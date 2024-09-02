from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    cal = HTMLCalendar().formatmonth(year, month_number)
    return render(request, 'home.html', {
        "year": year,
        "month": month,
        "cal": cal,
    })