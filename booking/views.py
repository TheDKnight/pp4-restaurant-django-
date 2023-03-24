from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItems, ConfirmedBooking
from .forms import BookingForm, BookingFormEdit
from django.contrib import messages

# Displays all the items in the menu items.
def menu(request):
    items = MenuItems.objects.all()
    return render(request, 'booking/menu.html', {'items': items})
   

# Creates a new booking and redirects the user
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

# Shows the booking list if the user is logged in and the user has made a booking, else it shows the html asking user to log in
def booking_list(request):
    if request.user.is_authenticated:
        bookings = ConfirmedBooking.objects.filter(user=request.user)
        context = {
        'bookings': bookings
        }
        return render(request, 'booking/booking.html', context)
    else:
        return render(request, 'booking/booking.html')

# The booking cancel view that gets the booking id if the user is logged in and has a booking and can cancel said booking
def booking_cancel(request, booking_id):
    booking = get_object_or_404(ConfirmedBooking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Your booking has been deleted successfully!')
        return redirect('booking')
    return render(request, 'booking/booking_cancel.html', {'booking': booking})

# The booking edit view that gets the booking id if the user is logged in and has a booking and can edit said booking
def booking_edit(request, booking_id):
    booking = get_object_or_404(ConfirmedBooking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingFormEdit(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been edited successfully!')
            return redirect('booking')
    else:
        form = BookingFormEdit(instance=booking)
    return render(request, 'booking/booking_edit.html', {'form': form})


# When url /home is called returns home.html
def home(request):
    return render(request, 'booking/home.html')

# When url /contact is called returns contact.html
def contact(request):
    return render(request, 'booking/contact.html')



