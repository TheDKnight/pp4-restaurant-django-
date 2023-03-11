from django.shortcuts import render
from .models import MenuItems

def menu(request):
    items = MenuItems.objects.all()
    return render(request, 'menu.html', {'items': items})



