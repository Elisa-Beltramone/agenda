from django import forms
from django.forms import ModelForm
from .models import Venue

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name_venue', 'address', 'zip_code', 'phone')