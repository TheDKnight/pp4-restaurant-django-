from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# The time slots that the users can select for a booking
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

# The number of guests that the user can select when making booking.
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

# The confirmed booking class that takes a user,day and time and number of guests from the above lists.


class ConfirmedBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_SLOTS, default="8pm")
    guests = models.CharField(max_length=20, choices=GUESS_SELECT, default="1")

    # The naming convention in the admin panel
    class Meta:
        verbose_name = "Confirmed Booking"
        verbose_name_plural = "Confirmed Bookings"

    # Returns these string data in the admin panel

    def __str__(self):
        return f' USER: {self.user} DATE: {self.day} TIME: {self.time} GUESTS: {self.guests}'


# The menuitems model takes vales if name, description and price


class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # The nanming convention in the admin panel
    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    # Returns the menu itmes names
    def __str__(self):
        return self.name
