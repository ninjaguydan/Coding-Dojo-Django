from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/show/new")
        else:
            Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['rdate'], desc = request.POST['desc'])
            return redirect("/shows")
    else:
        context = {
            "shows" : Show.objects.all()
        }
        return render(request, "index.html", context)

def create_show(request):
    return render(request, "create.html")

def destroy(request, show_id):
    show = Show.objects.get(id = show_id)
    show.delete()
    return redirect("/shows")

def update(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id), 
    }
    return render(request, "update.html", context)

def display(request, show_id):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/show/{show_id}/edit")
        else:
            updated_show = Show.objects.get(id=show_id)
            updated_show.title = request.POST['title']
            updated_show.network = request.POST['network']
            updated_show.release_date = request.POST['rdate']
            updated_show.desc = request.POST['desc']
            updated_show.save()
            return redirect(f"/show/{show_id}")
    else:
        context = {
            "show": Show.objects.get(id=show_id),
        }
        return render(request, "display.html", context)