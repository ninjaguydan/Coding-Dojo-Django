from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def logout(request):
    request.session.clear()
    return redirect('/')

def books(request):
    context = {
        "user" : User.objects.get(id = request.session['userid']),
        "reviews" : Review.objects.all(),
        "books" : Book.objects.all(),
        }
    return render(request,'books.html', context)

def addbook(request):
    context = {
        "user" : User.objects.get(id = request.session['userid']),
        "authors" : Author.objects.all(),
        }
    return render(request, "addbook.html", context)

def add(request):
    if request.method == "GET":
        return redirect('/books/addbook')
    errors = Book.objects.validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books/addbook')
    if request.POST['new_author']:
        author = Author.objects.create(name = request.POST['new_author'])
    else:
        author = Author.objects.create(name = request.POST['author'])
    user = User.objects.get(id = request.session['userid'])
    new_book = Book.objects.create(
        title= request.POST['title'], 
        desc = request.POST['desc'],
        author = author,
        added_by = user
        )
    Review.objects.create(
        content = request.POST['review'],
        rating = request.POST['rating'],
        book = new_book,
        user = user
        )
    return redirect('/books')
        
def display_book(request, book_id):
    book = Book.objects.get(id = book_id)
    user = User.objects.get(id = request.session['userid'])
    if request.method == "GET":
        context = {
            "user" : user,
            "book" : book,
        }
        return render(request, "reviews.html", context)
    errors = Review.objects.validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/books/{book_id}')
    Review.objects.create(
        content=request.POST['review'], 
        rating=request.POST['rating'],
        book=book,
        user=user
        )
    return redirect(f'/books/{book_id}')

def display_profile(request, profile_id):
    context = {
        "profile" : User.objects.get(id=profile_id),
        "user" : User.objects.get(id=request.session['userid']),
    }
    return render(request, "user.html", context)