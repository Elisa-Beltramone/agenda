from django.contrib import admin
from .models import Venue
from .models import AgendaUser
from .models import Event

admin.site.register(Venue)
admin.site.register(AgendaUser)
admin.site.register(Event)
