from django.shortcuts import get_object_or_404, render
from chat.models import Room, Message

# Create your views here.


def index(request):
    rooms = Room.objects.all()
    return render(request, "chat/index.html", context={"rooms" : rooms})


def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room)
    return render(request, "chat/room.html", context={"room" : room, "messages": messages})


def new_room(request):
    return render(request, "chat/new_room.html")
