from django.urls import path
from chat.views import index, room, new_room


urlpatterns = [
    path('', index, name="index"),
    path('room/new/', new_room, name="newroom"),
    path('room/<str:slug>/', room, name="room"),
]