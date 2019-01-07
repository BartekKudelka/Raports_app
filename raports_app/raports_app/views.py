from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from raports_app.polls.models import User


def home(request):
    return render(request, 'home.html')


def sign_up(request):
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')