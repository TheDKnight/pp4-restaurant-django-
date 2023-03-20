from django.urls import path
from .views import menu, home, contact, booking_list, booking_new

urlpatterns = [
    path("contact/", contact, name="contact"),
    path('menu/', menu, name="menu"),
    path('', home, name="home"),
    path('booking/', booking_list, name="booking"),
    path('booking/new/', booking_new, name="booking_new"),
]
