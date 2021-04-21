from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index),
    path('show/new', views.create_show),
    path('show/<int:show_id>/destroy', views.destroy),
    path('show/<int:show_id>/edit', views.update),
    path('show/<int:show_id>', views.display),
]