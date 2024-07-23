from django.urls import path
from . import views

app_name='app_schedules'
urlpatterns = [
    path('', views.index),
    path('overview/', views.overview),
    path('vehicle/', views.vehicle),
    path('result/', views.result),
]
