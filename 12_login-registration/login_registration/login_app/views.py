from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        print(f"the value being passed back is {request.POST['bdate']}")
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password = request.POST['pw']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            bdate = request.POST['bdate'],
            email = request.POST['email'],
            password = pw_hash,
        )
        return redirect("/welcome")

def welcome(request):
    return render(request, "welcome.html")

