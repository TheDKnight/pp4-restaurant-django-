from django.urls import path
from .views import menu, home, contact, booking_list, booking_new, booking_cancel

urlpatterns = [
    path("contact/", contact, name="contact"),
    path('menu/', menu, name="menu"),
    path('', home, name="home"),
    path('booking/', booking_list, name="booking"),
    path('booking/new/', booking_new, name="booking_new"),
    path('bookings/<int:booking_id>/cancel/', booking_cancel, name='booking_cancel'),
]
