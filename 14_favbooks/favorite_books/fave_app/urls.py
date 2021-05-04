from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('logout', views.logout),
    path('add', views.add),
]