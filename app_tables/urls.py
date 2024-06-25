from django.urls import path
from . import views

app_name="datatables"
urlpatterns = [
    path('outlets/', views.outlets_index, name='outlet'),
    path('outlets/create/', views.outlets_create, name='outletCreate'),
    path('outlets/update/', views.outlets_update, name='outletUpdate'),
    path('outlets/view/', views.outlets_view, name='outletView'),
    
    path('vehicles/', views.vehicles_index, name='vehicle'),
    path('vehicles/create', views.vehicles_create, name='vehicleCreate'),
    path('vehicles/update', views.vehicles_update, name='vehicleUpdate'),
    path('vehicles/view', views.vehicles_view, name='vehicleView'),
]
