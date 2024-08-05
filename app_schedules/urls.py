from django.urls import path
from . import views

app_name='app_schedules'
urlpatterns = [
    path('select-outlets', views.index, name='index'),
    path('confirm-outlets/', views.viewoutlets, name='viewoutlets'),
    path('selected-outlets/process-outlets/', views.processoutlets, name='processoutlets'),
    path('select-vehicles/', views.vehicles, name='vehicles'),
    path('select-drivers/', views.drivers, name='drivers'),
    # path('result/', views.result, name='results'),
    # path('overview/', views.overview),
]
