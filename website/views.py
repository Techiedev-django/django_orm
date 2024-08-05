from django.http import HttpResponse
from django.shortcuts import render

def homes(request):
    return HttpResponse('welcome to homes page')

def home(request):
    return render(request, 'home.html')
