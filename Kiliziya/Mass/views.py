from django.shortcuts import render
from .models import Mass
from .Massform import MassForm
# Create your views here.


def Misa(request):

    obj = Mass.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'mass.html', context)


def ShyiramoMissa(request):
    form = MassForm()
    if request.method == "POST":
        form = MassForm(request.POST)
        if form.is_valid():
            obj = Mass.objects.create(**form.cleaned_data)

    context = {
        'form': form
    }
    return render(request, 'missanew.html', context)
