from django.shortcuts import render
from .bapteme import Kwiyandikisha

# Create your views here.


def Home(request):
    return render(request, 'Ubukarani.html')


def Register(request):
    form = Kwiyandikisha(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'icyangombwa.html', {'form': form})
