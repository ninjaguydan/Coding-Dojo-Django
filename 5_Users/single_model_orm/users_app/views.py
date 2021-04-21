from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "users" : User.objects.all()
    }
    return render(request, "index.html", context)

def create_user(request):
    User.objects.create(
        first_name = request.POST['fname'], 
        last_name = request.POST['lname'],
        email = request.POST['email'],
        age = request.POST['age']
        )
    return redirect('/')