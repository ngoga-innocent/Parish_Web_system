from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Messaging, Room
from django.contrib.auth.decorators import login_required
# Create your views here.


def Home(request):
    staff = User.objects.filter(is_staff=True)
    context = {
        'staffs': staff
    }

    return render(request, 'chat_dashboard.html', context)


@login_required
def Rooms(request):
    users = User.objects.all()
    rooms = Room.objects.all()
    context = {
        'allrooms': rooms
    }
    for user in users:
        if user.is_staff:
            try:
                Room.objects.get(slug=user.username)
            except:
                Room.objects.create(name=user.first_name, slug=user.username)
    return render(request, 'chat_dashboard.html', context)


@login_required
def ChatRoom(request, id):
    rooms = Room.objects.all()
    room = Room.objects.get(id=id)
    messages = Messaging.objects.filter(reciever=room.slug)

    context = {
        'messages': messages,
        'allrooms': rooms,
        'room': room
    }

    if request.method == "POST":
        sender = request.POST['sender']
        receiver = request.POST['receiver']
        message = request.POST['message']
        time = request.POST['date']

        new_message = Messaging.objects.create(
            sender=sender, data=message, reciever=receiver, time=time)
        new_message.save()
        return render(request, 'chat.html', context)
    else:
        return render(request, 'chat.html', context)
