from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return HttpResponse("Login view")

def register_view(request):
    return HttpResponse("Register view")
