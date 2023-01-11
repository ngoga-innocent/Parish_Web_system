from django.shortcuts import render, redirect
from django.contrib import messages
from Ubukarani.models import Ibyasabwe, Icyangombwa
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def Home(request):
    pending = Ibyasabwe.objects.filter(status=1)

    context = {
        'pending': pending
    }
    return render(request, 'dashboard.html', context)


@login_required
def Pending(request):
    pending_docs = Ibyasabwe.objects.filter(status=1)
    pending = Ibyasabwe.objects.filter(status=1)
    context = {
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
