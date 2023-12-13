from django.http import HttpResponse
from django.shortcuts import render

def notes(request):
    return HttpResponse("Hello from Notes app!")
