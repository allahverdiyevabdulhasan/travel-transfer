from django import forms
from .models import Booking

class SearchForm(forms.Form):
    pickup_location = forms.CharField(label="Enter Pick-up location")
    destination = forms.CharField(label="Enter Destination")
    journey_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    return_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    passengers = forms.IntegerField(min_value=1, initial=1)
    flight_type = forms.ChoiceField(choices=[('oneway', 'One Way'), ('return', 'Return')], widget=forms.RadioSelect)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone_number']
