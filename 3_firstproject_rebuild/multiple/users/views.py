from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholser for users to log in")

def display(request):
    return HttpResponse("placeholder to later display a list of users")