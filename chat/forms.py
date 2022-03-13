from django import forms
from chat.models import Message, Room


class NewRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ('slug',)

"""
    explicitly add init and save methods to handle message saving issues
"""
class NewMessageForm(forms.ModelForm):
    def __init__(self, **kwargs):
        self.room = kwargs.pop('room', None)
        self.author = kwargs.pop('author', None)
        super(NewMessageForm, self).__init__(**kwargs)

    def save(self, commit=True):
        obj = super(NewMessageForm, self).save(commit=False)
        obj.room = self.room
        obj.author = self.author
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Message
        fields = ("content", )