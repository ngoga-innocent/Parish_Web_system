from django.shortcuts import render, redirect
from django.http import HttpResponse
from Announcements.models import Announcements
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import time
from Events.models import Event
# Create your views here.


def Home(request):
    events = Event.objects.all()
    announcements = Announcements.objects.all().order_by('-id')[:4]
    announcementss = Announcements.objects.all().order_by('id')[:4]

    context = {
        'announcementss': announcementss,
        'events': events,
        'announcents': announcements
    }
    return render(request, 'home.html', context)


@login_required
def sendmail(request):
    if request.method == "POST":
        name = request.POST['fullname']
        email = request.POST['email']
        msg = request.POST['message']

        send_mail(name, msg, 'bienvenueinnocent2000@gmail.com', [email])
        messages.info(request, 'Thanks for contacting us!!!')
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


def Afterpay(request):
    time.sleep(60)
    return redirect(request, 'home.html')


def About(request):
    return render(request, 'about.html')
