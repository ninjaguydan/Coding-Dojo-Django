from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('wall/post_message', views.post_message),
    path('wall/destroy_message', views.destroy_message),
    path('wall/post_comment', views.post_comment),
]