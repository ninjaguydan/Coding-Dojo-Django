from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>/comments', views.comments),
    path('<int:id>/comments/delete', views.delete_comment),
    path('<int:id>/confirm', views.confirm_delete),
    path('<int:id>/destroy', views.delete),
]