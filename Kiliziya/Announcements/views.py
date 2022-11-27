from django.shortcuts import render
from .models import Announcements
from .createann import AnnouncementsForm

# Create your views here.


def CreateAnnouncements(request):
    form = AnnouncementsForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()

    return render(request, 'create.html', {'form': form})


def Announcement(request):

    announcements = Announcements.objects.all()
    return render(request, 'announcements.html', {'announcements': announcements})


def Announcement_detail(request, id):
    announcement = Announcements.objects.get(id=id)
    return render(request, 'detail.html', {'announcement': announcement})
