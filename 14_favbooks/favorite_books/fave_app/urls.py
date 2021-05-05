from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('logout', views.logout),
    path('add', views.add),
    path('<int:book_id>', views.display_book),
    path('<int:book_id>/fav', views.favorite),
    path('<int:book_id>/unfav', views.unfavorite),
    path('<int:book_id>/update', views.update),
    path('<int:book_id>/delete', views.delete),
    path('<int:user_id>/profile', views.profile),
]