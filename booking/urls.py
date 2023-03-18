from django.urls import path
from .views import menu, home, contact, booking

urlpatterns = [
    path("contact/", contact, name="contact"),
    path('menu/', menu, name="menu"),
    path('', home, name="home"),
    path('booking/', booking, name="booking"),
]
