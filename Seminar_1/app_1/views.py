from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Hello, world!</h1>")

def about(request):
    return HttpResponse("<h3>About us</h3>")
