#from django.db import models

# Create your models here.
#from django.db import models
#from django.contrib.auth.models import AbstractUser

#class User(AbstractUser):
#    ROLE_CHOICES = (
#        ('admin', 'Admin'),
#        ('organizer', 'Organizer'),
#        ('attendee', 'Attendee'),
#    )
#    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

#class Event(models.Model):
#    title = models.CharField(max_length=100)
#    description = models.TextField(blank=True, null=True)
#    date = models.DateTimeField()
#    location = models.CharField(max_length=255, blank=True, null=True)
#    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

#class Booking(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    event = models.ForeignKey(Event, on_delete=models.CASCADE)
#    timestamp = models.DateTimeField(auto_now_add=True)

# events/models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')

    def __str__(self):
        return self.user.username

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
