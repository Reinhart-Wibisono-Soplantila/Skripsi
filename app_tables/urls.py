from django.urls import path
from . import views

app_name="app_tables"
urlpatterns = [
    path('outlets/', views.outlet_index, name='outletIndex'),
    path('outlets/create/', views.outlet_create, name='outletCreate'),
    path('outlets/update/', views.outlet_update, name='outletUpdate'),
    path('outlets/view/', views.outlet_view, name='outletView'),
    
    path('vehicles/', views.vehicle_index, name='vehicleIndex'),
    path('vehicles/create', views.vehicle_create, name='vehicleCreate'),
    path('vehicles/update/<str:vehicleNumber>', views.vehicle_update, name='vehicleUpdate'),
    path('vehicles/delete/<str:vehicleNumber>', views.vehicle_delete, name='vehicleDelete'),
    
    path('driver/create', views.driver_create, name='driverCreate'),
    # path('driver/update', views.driver_update, name='driverUpdate'),
    # path('driver/view', views.driver_view, name='driverView'),
]
