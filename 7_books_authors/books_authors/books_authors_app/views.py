from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "books" : Book.objects.all(),
    }
    return render(request, "index.html", context)

def author_index(request):
    context = {
        "authors": Author.objects.all(),
    }
    return render(request, "authors.html", context)

def add_book(request):
    Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect("/")

def add_author(request):
    Author.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], notes = request.POST['notes'])
    return redirect("/author_index")

def display_book(request, book_id):
    book = Book.objects.get(id = book_id)
    excluded = Author.objects.exclude(books = book)
    context = {
        "book": book,
        "authors": book.authors.all(),
        "excluded_authors": excluded,
    }
    return render(request, "books.html", context)

def display_author(request, author_id):
    author = Author.objects.get(id = author_id)
    excluded = Book.objects.exclude(authors = author)
    context = {
        "author": author,
        "books": author.books.all(),
        "excluded_books": excluded,
    }

    return render(request, "display-authors.html", context)

def append_book(request, author_id):
    author = Author.objects.get(id = author_id)
    book_to_add = Book.objects.get(title = request.POST['books'])
    author.books.add(book_to_add)
    return redirect(f"/author_index/{author_id}")

def append_author(request, book_id):
    book = Book.objects.get(id = book_id)
    author_to_add = Author.objects.get(first_name = request.POST['authors']) 
    book.authors.add(author_to_add)
    return redirect(f"/books/{book_id}")

def remove_all_authors(request, book_id):
    book = Book.objects.get(id = book_id)
    all_authors = Author.objects.all()
    for author in all_authors:
        book.authors.remove(author)
    return redirect(f"/books/{book_id}")

def remove_all_books(request, author_id):
    author = Author.objects.get(id = author_id)
    all_books = Book.objects.all()
    for book in all_books:
        author.books.remove(book)
    return redirect(f"/author_index/{author_id}") 