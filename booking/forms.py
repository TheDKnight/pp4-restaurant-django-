from django import forms
from .models import ConfirmedBooking, TIME_SLOTS, GUESS_SELECT

class BookingForm(forms.ModelForm):
    time = forms.ChoiceField(choices=TIME_SLOTS)
    guests = forms.ChoiceField(choices=GUESS_SELECT)

    class Meta:
        model = ConfirmedBooking
        fields = ('day', 'time', 'guests')