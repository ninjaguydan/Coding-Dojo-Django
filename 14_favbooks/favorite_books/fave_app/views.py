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

def display_book(request, book_id):
    context = {
        "book" : Book.objects.get(id = book_id),
        "user" : User.objects.get(id = request.session['userid'])
    }
    return render(request, "fav_books.html", context)

def favorite(request, book_id):
    user = User.objects.get(id = request.session['userid'])
    book = Book.objects.get(id = book_id)
    user.books.add(book)
    return redirect(f'/books/{book_id}')

def unfavorite(request, book_id):
    user = User.objects.get(id = request.session['userid'])
    book = Book.objects.get(id = book_id)
    user.books.remove(book)
    return redirect(f'/books/{book_id}')

def update(request, book_id):
    if request.method == "GET":
        return redirect(f'/books/{book_id}')
    book = Book.objects.get(id = book_id)
    book.title = request.POST['title']
    book.desc = request.POST['desc']
    book.save()
    return redirect('/books')

def delete(request, book_id):
    book = Book.objects.get(id = book_id)
    book.delete()
    return redirect('/books')

def profile(request, user_id):
    context = {
        "profile" : User.objects.get(id = user_id),
        "user" : User.objects.get(id = request.session['userid'])
    }
    return render(request, "user.html", context)