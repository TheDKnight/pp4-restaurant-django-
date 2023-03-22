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
    ("10:30 PM", "10:30 PM"),
    ("11 PM", "11 PM"),
    ("11:30 PM", "11:30 PM"),
)

GUESS_SELECT = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
)


class ConfirmedBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_SLOTS, default="8pm")
    guests = models.CharField(max_length=20, choices=GUESS_SELECT, default="1")

    class Meta:
        verbose_name = "Confirmed Booking"
        verbose_name_plural = "Confirmed Bookings"


    def __str__(self):
        return self.title, self.user


class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
    

    def __str__(self):
        return self.name

