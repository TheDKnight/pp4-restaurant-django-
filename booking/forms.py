from django import forms
from .models import ConfirmedBooking, TIME_SLOTS, GUESS_SELECT

# The booking form that allows a user to select the time guests and return the value


class BookingForm(forms.ModelForm):
    time = forms.ChoiceField(choices=TIME_SLOTS)
    guests = forms.ChoiceField(choices=GUESS_SELECT)

    class Meta:
        model = ConfirmedBooking
        fields = ('day', 'time', 'guests')

# The booking form that allows the user to edit there own booking after is it created


class BookingFormEdit(forms.ModelForm):
    class Meta:
        model = ConfirmedBooking
        fields = ('day', 'time', 'guests')
