from django import forms
from chat.models import Room


class NewRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ('slug',)