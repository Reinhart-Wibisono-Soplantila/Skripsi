from django.urls import path
from . import views

app_name='app_schedules'
urlpatterns = [
    path('', views.index, name='index'),
    path('selected-outlets/', views.viewoutlets, name='viewoutlets'),
    path('process-outlets/', views.processoutlets, name='processoutlets'),
    path('overview/', views.overview),
    path('vehicle/', views.vehicle),
    path('result/', views.result),
]
