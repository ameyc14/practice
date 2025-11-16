from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse("<h1>My first django</h1>")

def displayDatetime(request):
    dt=datetime.datetime.now()
    s="<b>Current datetime</b>"+str(dt)
    return HttpResponse(s)
