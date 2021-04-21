from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        # validation
        errors = Course.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            new = Course.objects.create(name = request.POST['name'])
            Description.objects.create(content = request.POST['desc'], course = new)
            return redirect('/')
    else:
        context = {
            "courses" : Course.objects.all(),
        }
        return render(request, "index.html", context)

def confirm_delete(request, id):
    context = {
        "course" : Course.objects.get(id=id),
    }
    return render(request, "destroy.html", context)

def comments(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        errors = Comment.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/{id}/comments")
        else:
            Comment.objects.create(content = request.POST['comment'], course = course)
            return redirect(f"/{id}/comments")
    else:
        context = {
            "course" : course,
        }
        return render(request, "comments.html", context)

def delete(request, id):
    Course.objects.get(id = id).delete()
    return redirect("/")

def delete_comment(request, id):
    comment = Comment.objects.get(id = id)
    course_id = comment.course.id
    comment.delete()
    return redirect(f"/{course_id}/comments")
        