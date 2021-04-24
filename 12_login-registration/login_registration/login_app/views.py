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

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect("/welcome")
    return redirect("/")

def welcome(request):
    if 'userid' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['userid'])
    context = {'user': user }
    return render(request, 'welcome.html', context)

def logout(request):
    request.session.clear()
    return redirect("/")

