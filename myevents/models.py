from django.db import models

class Venue(models.Model):
    name_venue = models.CharField('Venue name', max_length=120)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=15)
    phone = models.CharField('Contact Phone', max_length=12, blank=True)

    def __str__(self):
        return self.name_venue
    
class AgendaUser(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField('User email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name_event = models.CharField('Event name', max_length=120)
    date_event = models.DateTimeField('Event date')
    venue_event = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager_event = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(AgendaUser, blank=True)

    def __str__(self):
        return self.name_event