from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event
from .forms import VenueForm

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    today = datetime.now().day
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    cal = HTMLCalendar().formatmonth(year, month_number)
    return render(request, 'home.html', {
        "year": year,
        "month": month,
        "cal": cal,
        "today": today,
    })

def planner(request):
    event_list = Event.objects.all()
    return render(request, 'myPlanner.html', {'event_list':event_list})

def add_event(request):
    today = datetime.now().day
    wday = datetime.now().strftime('%A')
    month=datetime.now().strftime('%B')
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            time_now = datetime.now()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = VenueForm
        if submitted in request.GET:
            submitted = True
    return render(request, 'newEvent.html', {
        'today':today, 
        'wday': wday, 
        'month':month, 
        'form':form,
        'submitted':submitted,
        'time_now':time_now
        })

def show_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'showEvent.html', {'event':event})

def searched(request):
    if request.method == "POST":
        searching = request.POST['searching']
        return render(request, 'searchs.html', {'searching':searching})
    else:
        return render(request, 'searchs.html', {})