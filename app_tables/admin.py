from django.contrib import admin
from .models import VehicleModel, DriverModel

# Register your models here.
admin.site.register(VehicleModel)
admin.site.register(DriverModel)