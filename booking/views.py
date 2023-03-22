from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItems, ConfirmedBooking
from .forms import BookingForm, BookingFormEdit
from django.contrib import messages


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
            messages.success(request, 'Your booking has been added successfully!')
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

def booking_cancel(request, booking_id):
    booking = get_object_or_404(ConfirmedBooking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Your booking has been deleted successfully!')
        return redirect('booking')
    return render(request, 'booking/booking_cancel.html', {'booking': booking})

    
def booking_edit(request, booking_id):
    booking = get_object_or_404(ConfirmedBooking, id=booking_id)
    if request.method == 'POST':
        form = BookingFormEdit(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been edited successfully!')
            return redirect('booking')
    else:
        form = BookingFormEdit(instance=booking)
    return render(request, 'booking/booking_edit.html', {'form': form})


def home(request):
    return render(request, 'booking/home.html')


def contact(request):
    return render(request, 'booking/contact.html')



