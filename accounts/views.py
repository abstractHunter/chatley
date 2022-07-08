from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

# Create your views here.


User = get_user_model()


def signup(request):
    if request.method == "POST":
        """
            if the request method is POST:
                get the values provided
                create the user with provided credentials
                log the user in
                redirect user to home page
        """
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password_confirm")
        
        if not username:
            return render(request, "accounts/signup.html", {"error": "Username is required", "old_username": username})
        
        if User.objects.filter(username=username).exists():
            return render(request, "accounts/signup.html", {"error": "Username already exists", "old_username": username})

        if not (password and password2):
            return render(request, "accounts/signup.html", {"error": "Password is required", "old_username": username})
        
        if not password == password2:
            return render(request, "accounts/signup.html", {"error": "Passwords do not match", "old_username": username})
        
        user = User.objects.create_user(
            username=username,
            password=password,
        )
        login(request, user)
        return redirect("index")

    return render(request, "accounts/signup.html")


def signin(request):
    if request.method == "POST":
        """
            if the request method is POST:
                get the values provided
                check if a user with these credentials exits
                log the user in
                redirect user to home page
        """
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
        
        return render(request, "accounts/signin.html", {"error": "Invalid credentials", "old_username": username})

    return render(request, "accounts/signin.html")


def signout(request):
    logout(request)
    return redirect("index")

