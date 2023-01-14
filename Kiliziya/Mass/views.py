from django.shortcuts import render
from .models import Mass
from .Massform import MassForm
from django.utils.timezone import datetime
from datetime import date
from Events.models import Event
from Announcements.models import Announcements
from Ubukarani.models import Ibyasabwe
from Messaging.models import Messaging
# Create your views here.


def Misa(request):
    today = date.today()
    obj = Mass.objects.all().order_by('date', 'time')
    context = {
        'obj': obj,
        'today': today
    }
    return render(request, 'mass.html', context)


def ShyiramoMissa(request):
    unread = Messaging.objects.filter(
        receiver=request.user.username, status='1').count()
    pending = Ibyasabwe.objects.filter(status=1)
    form = MassForm()
    if request.method == "POST":
        form = MassForm(request.POST)
        if form.is_valid():
            obj = Mass.objects.create(**form.cleaned_data)

    context = {
        'unread': unread,
        'pending': pending,
        'form': form
    }
    return render(request, 'missanew.html', context)


def Mass_detail(request, myid):
    event = Event.objects.all().order_by('-date')
    announcements = Announcements.objects.all()
    mass = Mass.objects.get(id=myid)
    context = {
        'mass': mass,
        'events': event,
        'announcements': announcements
    }
    return render(request, 'mass_detail.html', context)
