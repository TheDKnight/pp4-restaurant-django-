from django.shortcuts import render, redirect
from .models import MenuItems, ConfirmedBooking
from .forms import BookingForm

def menu(request):
    items = MenuItems.objects.all()
    return render(request, 'booking/menu.html', {'items': items})
   

def booking_new(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('/booking')
    else:
        form = BookingForm()

    return render(request, 'booking/booking_new.html', {'form': form})


def booking_list(request):
    bookings = ConfirmedBooking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/booking.html', context)


def home(request):
    return render(request, 'booking/home.html')


def contact(request):
    return render(request, 'booking/contact.html')



