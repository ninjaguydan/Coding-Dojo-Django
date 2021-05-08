from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('logout', views.logout),
    path('addbook', views.addbook),
    path('addbook/add', views.add),
    path('<int:book_id>', views.display_book),
    path('<int:book_id>/favorite', views.favorite_book),
    path('<int:book_id>/unfavorite', views.unfavorite_book),
    path('<int:book_id>/delete', views.delete_book),
    path('users/<int:profile_id>', views.display_profile),
    path('review/<int:review_id>', views.delete_review),
    path('review/<int:review_id>/like', views.likes),
]