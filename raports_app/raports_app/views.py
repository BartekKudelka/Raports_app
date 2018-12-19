from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1> Witaj na stronie głównej generatora raportów</h1>")

def sign_up(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')