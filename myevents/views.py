from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

def home(request, year, month):
    return render(request, 'home.html', {
        "year": year,
        "month": month,
    })