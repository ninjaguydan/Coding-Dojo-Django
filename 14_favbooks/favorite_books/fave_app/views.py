from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def logout(request):
    request.session.clear()
    return redirect("/")

def books(request):
    user = User.objects.get(id = request.session["userid"])
    context = {
        "user" : user,
        "books" : Book.objects.all(),
        }
    return render(request, 'books.html',context)

def add(request):
    if request.method == "GET":
        return redirect('/books')
    errors = Book.objects.validator(request.POST)
    if errors:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    user = User.objects.get(id = request.session["userid"])
    new_book = Book.objects.create(title = request.POST['title'], desc = request.POST['desc'], uploaded_by = user)
    user.books.add(new_book)
    return redirect('/books')