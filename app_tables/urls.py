from django.urls import path
from . import views

urlpatterns = [
    path('outlets/', views.outlets_index),
    path('outlets/create/', views.outlets_create),
    path('outlets/update/', views.outlets_update),
    path('outlets/view/', views.outlets_view),
    
    path('vehicles/', views.vehicles_index),
    path('vehicles/create', views.vehicles_create),
    path('vehicles/update', views.vehicles_update),
    path('vehicles/view', views.vehicles_view),
]
