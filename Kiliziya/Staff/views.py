from Announcements.models import Announcements
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from Ubukarani.models import Ibyasabwe, Icyangombwa
from Messaging.models import Messaging
from Events.models import Event
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def Home(request):
    events = Event.objects.all().count()
    announcements = Announcements.objects.all().count()
    unread = Messaging.objects.filter(
        receiver=request.user.username, status='1').count()
    pending = Ibyasabwe.objects.filter(status=1)
    ibyangombwa = Icyangombwa.objects.all().count()
    users = User.objects.all().count()
    staffs = User.objects.filter(is_staff=True).count()

    context = {
        'events': events,
        'users': users,
        'staffs': staffs,
        'announcements': announcements,
        'icyangombwa': ibyangombwa,
        'unread': unread,
        'pending': pending
    }
    return render(request, 'homedashboard.html', context)


@login_required
def Pending(request):
    unread = Messaging.objects.filter(
        receiver=request.user.username, status='1').count()
    pending_docs = Ibyasabwe.objects.filter(status=1)
    pending = Ibyasabwe.objects.filter(status=1)
    context = {
        'unread': unread,
        'pending': pending,
        'pending_docs': pending_docs
    }
    return render(request, 'pending.html', context)


@login_required
def Review(request, id):
    pending = Ibyasabwe.objects.filter(status=1)
    doc = Ibyasabwe.objects.get(id=id)
    context = {
        'pending': pending,
        'doc': doc
    }
    return render(request, 'view.html', context)


@login_required
def Approve(request, id):
    doc = Ibyasabwe.objects.get(id=id)
    if request.method == 'POST':
        doc.status = 2
        doc.save()
        messages.info(request, 'successfully approved')
        return redirect('pending')
    else:
        return redirect('pending')
