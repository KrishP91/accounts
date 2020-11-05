from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from accounts.forms import roomForm, maidForm, roomListForm
from django.http import HttpResponse
from accounts.models import *


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'accounts/yes.html')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff() == True:
                return render(request, 'accounts/newrooms.html')
            return render(request, 'accounts/loggedin.html')
            
    elif request.user.is_authenticated:
        return render(request, 'accounts/loggedin.html')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'accounts/login.html')


def formView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = roomForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('A new room has been added.')
        else:
            form = roomForm()
        context = {
                'form' : form,
            }
        return render(request, 'accounts/newrooms.html', context)
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

def maidView(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = maidForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('A new maid has been added.')
        else:
            form = maidForm()
        context = {
                'form' : form,
            }
        return render(request, 'accounts/addmaids.html', context)
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

def roomListView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = roomListForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('Updated')
        else:
            data = Room.objects.all()
            form = roomListForm()
            room = {
                "num" : data,
                "form" : form
            }
            return render(request, 'accounts/roomstatus.html', room)
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
