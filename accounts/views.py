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

    return render(request, "accounts/signin.html")


def signout(request):
    logout(request)
    return redirect("index")

