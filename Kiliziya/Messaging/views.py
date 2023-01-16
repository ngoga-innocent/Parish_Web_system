from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Messaging, Room
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.


@login_required
def Home(request):
    staffs = User.objects.filter(is_staff=True).exclude(id=request.user.id)
    unread = Messaging.objects.filter(
        receiver=request.user.username, status='1').count()
    new_messages = Room.objects.filter(
        Q(client=request.user.username) | Q(staff=request.user.username))
    # print(new_messages)
    context = {
        'unread': unread,
        'staffs': staffs,
        'new_messages': new_messages

    }

    return render(request, 'homechat.html', context)


@login_required
def StaffCheck(request, id):
    staffs = User.objects.filter(is_staff=True).exclude(id=request.user.id)
    new_messages = Room.objects.filter(
        staff=request.user.username)

    staff = User.objects.get(id=id)
    room = Room.objects.filter(
        staff=staff.username, client=request.user.username)
    if room.exists():
        room = Room.objects.get(staff=staff.username,
                                client=request.user.username)
        client = request.user.username
        staff = room.staff
        slug = str(client) + str(staff)
        messages = Messaging.objects.filter(room=slug)
        context = {
            'staffs': staffs,
            'new_messages': new_messages,
            'room': room,
            'messages': messages
        }
        return render(request, 'chat.html', context)
    else:
        name = request.user.username
        slug = slug = str(name) + str(staff.username)
        new_room = Room.objects.create(
            name=name, slug=slug, staff=staff.username, client=name)
        new_room.save()
        room = Room.objects.get(
            staff=staff.username, client=request.user.username)
        client = request.user.username
        staff = room.staff
        slug = str(client) + str(staff)
        messages = Messaging.objects.filter(room=slug)
        context = {
            'staffs': staffs,
            'new_messages': new_messages,
            'room': room,
            'messages': new_messages
        }
        return render(request, 'chat.html', context)


@login_required
def ChatRoom(request, id):
    staffs = User.objects.filter(is_staff=True).exclude(id=request.user.id)
    new_messages = Room.objects.filter(
        staff=request.user.username)
    if Room.objects.filter(id=id).exists():
        rooms = Room.objects.get(id=id)
        name = rooms.client
        staff = rooms.staff
        slug = str(name) + str(staff)
        messages = Messaging.objects.filter(room=slug)
        message = Messaging.objects.filter(room=slug).update(status='2')
        client_pending = rooms.client_pending
        staff_pending = rooms.staff_pending
        if rooms.staff == request.user.username:
            staff_pending = 0
            room = Room.objects.filter(id=id).update(
                staff_pending=staff_pending)
        else:
            client_pending = 0
            room = Room.objects.filter(id=id).update(
                client_pending=client_pending)
        if request.method == "POST":
            sender = request.POST['sender']
            room = request.POST['room']
            data = request.POST['message']
            receiver = request.POST['receiver']

            new_message = Messaging.objects.create(
                sender=sender, room=room, data=data, receiver=receiver)
            if rooms.staff == request.user.username:
                client_pending = client_pending+1
                room = Room.objects.filter(id=id).update(
                    client_pending=client_pending)
                new_message.save()
            else:
                staff_pending = staff_pending+1
                room = Room.objects.filter(id=id).update(
                    staff_pending=staff_pending)
                new_message.save()
            context = {
                'new_messages': new_messages,
                'staffs': staffs,
                'room': rooms,
                'messages': messages
            }
            return render(request, 'chat.html', context)
        else:

            context = {
                'new_messages': new_messages,
                'staffs': staffs,
                'room': rooms,
                'messages': messages
            }
            return render(request, 'chat.html', context)
    else:
        new_messages = Room.objects.filter(
            Q(staff=request.user.username) | Q(client=request.user.username))
        name = request.user.username
        staff = User.objects.get(id=id)
        slug = str(name) + str(staff.username)
        new_room = Room.objects.create(
            name=name, slug=slug, staff=staff.username, client=name)
        new_room.save()

        context = {
            'new_messages': new_messages,
            'staff': staff
        }
        return render(request, 'chat.html', context)
