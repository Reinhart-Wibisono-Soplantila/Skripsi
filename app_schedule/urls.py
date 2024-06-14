from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('overview/', views.overview),
    path('vehicle/', views.vehicle),
    path('result/', views.result),
]
