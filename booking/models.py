from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.


TIME_SLOTS = (
    ("8 PM", "8 PM"),
    ("8:30 PM", "8:30 PM"),
    ("9 PM", "9 PM"),
    ("9:30 PM", "9:30 PM"),
    ("10 PM", "10 PM"),
)

GUESS_SELECT = (
    ("1","1"),
    ("2","2")

)


class ConfirmedBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_SLOTS, default="8pm")
    guests = models.CharField(max_length=20, choices=GUESS_SELECT, default="1")
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)


def __str__(self):
    return self.title, self.user