from django.contrib import admin
from .models import Venue
from .models import AgendaUser
from .models import Event

admin.site.register(AgendaUser)
admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name_venue', 'address',)
    ordering= ('name_venue',)
    search_fields= ('name_venue', 'address')
    list_filter = ('address',)