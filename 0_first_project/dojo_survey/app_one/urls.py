from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('handler/', views.handler),
    path('result/', views.result),
]