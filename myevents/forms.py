from django import forms
from django.forms import ModelForm
from .models import Venue, Event

# class VenueForm(ModelForm):
#     class Meta:
#         model = Venue
#         fields = ('name_venue', 'address', 'zip_code', 'phone')

class VenueForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name_event', 'date_event', 'venue_event', 'description')