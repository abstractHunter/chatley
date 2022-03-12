from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

import string
import random

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=6, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _get_unique_slug(self):
        """
        generate a unique slug for each room
        """
        length = 6

        while True:
            slug = "".join(random.choices(string.ascii_uppercase, k=length))
            if Room.objects.filter(slug=slug).count() == 0:
                break

        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("room", kwargs={"slug" : self.slug})


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,  related_name="messages")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
