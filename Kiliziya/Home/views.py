from django.shortcuts import render
from django.http import HttpResponse
from Announcements.models import Announcements


# Create your views here.
def Home(request):
    announcements = Announcements.objects.all()

    context = {
        'announcents': announcements
    }
    return render(request, 'home.html', context)
