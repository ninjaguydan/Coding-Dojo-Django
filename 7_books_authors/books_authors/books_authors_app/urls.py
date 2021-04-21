from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('author_index', views.author_index),
    path('author_index/add_author', views.add_author),
    path('author_index/<int:author_id>', views.display_author),
    path('author_index/<int:author_id>/append', views.append_book),
    path('author_index/<int:author_id>/remove', views.remove_all_books),
    path('books/<int:book_id>', views.display_book),
    path('books/<int:book_id>/append', views.append_author),
    path('books/<int:book_id>/remove', views.remove_all_authors),
]