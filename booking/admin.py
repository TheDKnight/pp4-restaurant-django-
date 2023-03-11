from django.contrib import admin
from .models import ConfirmedBooking
from .models import MenuItems

# Register your models here.
admin.site.register(ConfirmedBooking)
admin.site.register(MenuItems)