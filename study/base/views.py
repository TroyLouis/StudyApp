from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Hello Troy')

def room(request):
    return HttpResponse('ROOM')

def hello(request):
    return HttpResponse("Hello")
