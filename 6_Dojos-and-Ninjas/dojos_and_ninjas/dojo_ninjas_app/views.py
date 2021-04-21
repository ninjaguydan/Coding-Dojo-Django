from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "dojos": Dojo.objects.all(),
    }
    return render(request, "index.html", context)

def create_dojo(request):
    Dojo.objects.create(name = request.POST['name'], city = request.POST['city'] , state = request.POST['state'])
    return redirect("/")

def create_ninja(request):
    dojo = Dojo.objects.get(name = request.POST['dojos'])
    Ninja.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], dojo = dojo)
    return redirect("/")

def delete(request, dojo_name):
    dojo = Dojo.objects.get(name = dojo_name)
    dojo.ninjas.all().delete()
    dojo.delete()
    return redirect("/")