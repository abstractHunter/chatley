from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from chat.models import Room, Message
from chat.forms import NewRoomForm

# Create your views here.


def index(request):
    rooms = Room.objects.all()
    return render(request, "chat/index.html", context={"rooms" : rooms})


@login_required(login_url="signin")
def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room)
    return render(request, "chat/room.html", context={"room" : room, "messages": messages})


@login_required(login_url="signin")
def new_room(request):
    if request.method == 'POST':
        form = NewRoomForm(request.POST)

        if form.is_valid():
            room = form.save()
            return redirect("room", room.slug)
    else:
        form = NewRoomForm()

    return render(request, "chat/new_room.html", context={"form" : form})
