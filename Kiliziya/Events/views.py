from django.shortcuts import render, redirect
from .models import Event
import datetime
# Create your views here.


def Home(request):
    event = Event.objects.all().order_by('-date')

    context = {
        'events': event
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
