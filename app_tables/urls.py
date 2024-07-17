from django.urls import path
from . import views

app_name="app_tables"
urlpatterns = [
    path('outlets/', views.outlet_index, name='outletIndex'),
    path('outlets/create/', views.outlet_create, name='outletCreate'),
    path('outlets/update/<str:outletCode>', views.outlet_update, name='outletUpdate'),
    path('outlets/view/<str:outletCode>', views.outlet_view, name='outletView'),
    path('outlets/delete/<str:outletCode>', views.outlet_delete, name='outletDelete'),
    
    path('vehicles/', views.vehicle_index, name='vehicleIndex'),
    path('vehicles/create', views.vehicle_create, name='vehicleCreate'),
    path('vehicles/update/<str:vehicleNumber>', views.vehicle_update, name='vehicleUpdate'),
    path('vehicles/delete/<str:vehicleNumber>', views.vehicle_delete, name='vehicleDelete'),
    
    path('driver/create', views.driver_create, name='driverCreate'),
    path('driver/update/<str:driverId>', views.driver_update, name='driverUpdate'),
    path('driver/view/<str:driverId>', views.driver_view, name='driverView'),
    path('driver/delete/<str:driverId>', views.driver_delete, name='driverDelete'),
    
    path('ajax/load-regencies/', views.load_regencies, name='ajax_load_regencies'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-villages/', views.load_villages, name='ajax_load_villages'),
]
