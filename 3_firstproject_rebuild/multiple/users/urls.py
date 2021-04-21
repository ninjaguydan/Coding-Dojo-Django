from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.index),
    path('login/', views.login),
    path('new/', views.index),
    path('users/', views.display),
]