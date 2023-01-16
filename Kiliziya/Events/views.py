from django.shortcuts import render, redirect
from .models import Event
import datetime
from Announcements.models import Announcements

# Create your views here.


def Home(request):
    event = Event.objects.all().order_by('-date')
    announcements = Announcements.objects.all()
    context = {
        'events': event,
        'announcents': announcements
    }
    return render(request, 'events.html', context)


def NewEvent(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        # daten = date.strftime("%y/%b/%d")
        thumb = request.FILES['thumb']

        event = Event(title=title, description=description,
                      date=date, thumb=thumb)
        event.save()

        return redirect('/')
    else:
        return render(request, 'newevent.html')


def event_detail(request, id):
    events = Event.objects.get(id=id)

    context = {
        'event': events
    }
    return render(request, 'event_detail.html', context)
