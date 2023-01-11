from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def Home(request):
    return render(request, 'user.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.is_staff:
                return redirect('/staff')
            else:
                return redirect('/')
        else:
            messages.info(request, 'username or password is not correct')
            return redirect('login')
    else:
        return render(request, 'login.html')


def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        is_staff = request.POST['is_staff']

        context = {

        }

        if password1 == password2:
            if User.objects.filter(username=username).exists():

                messages.info(request, 'Username already exists')
                return redirect('.')
            else:

                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1, is_staff=False)
                messages.info(request, 'Succesfully registered')
                user.save()
                return redirect('/')
        else:
            print('password does not match')
            messages.info(request, 'Passwords does not match')
            return redirect('.')

    else:
        return render(request, 'register.html')


def edit(request, myid):
    usersel = User.objects.get(id=myid)
    context = {
        'user': usersel
    }
    return render(request, 'register.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')
