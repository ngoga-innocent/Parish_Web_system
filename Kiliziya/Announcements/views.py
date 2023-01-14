from django.shortcuts import render
from .models import Announcements
from .createann import AnnouncementsForm
from Ubukarani.models import Ibyasabwe
from Messaging.models import Messaging

# Create your views here.


def CreateAnnouncements(request):
    unread = Messaging.objects.filter(
        receiver=request.user.username, status='1').count()
    pending = Ibyasabwe.objects.filter(status=1)
    form = AnnouncementsForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'unread': unread,
        'pending': pending
    }
    return render(request, 'create.html', context)


def Announcement(request):

    announcements = Announcements.objects.all().order_by('-id').values()
    return render(request, 'announcements.html', {'announcements': announcements})


def Announcement_detail(request, id):
    announcement = Announcements.objects.get(id=id)
    return render(request, 'detail.html', {'announcement': announcement})
