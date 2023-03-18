from django.urls import path
from .views import menu, home, contact

urlpatterns = [
    path("contact/", contact, name="contact"),
    path('menu/', menu, name="menu"),
    path('', home, name="home"),
]
