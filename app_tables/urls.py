from django.urls import path
from . import views

urlpatterns = [
    path('outlets/', views.outlets_index),
    path('vehicles/', views.vehicles_index),
    path('outlets/create/', views.outlets_create)
]
