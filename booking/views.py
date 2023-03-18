from django.shortcuts import render, redirect
from .models import MenuItems


def menu(request):
    items = MenuItems.objects.all()
    return render(request, 'booking/menu.html', {'items': items})
    # return render(request, 'booking/menu.html')


def home(request):
    return render(request, 'booking/home.html')

def contact(request):
    return render(request, 'booking/contact.html')

