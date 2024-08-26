from django.shortcuts import render
from django.views.generic import View
from app_outlet.models import OutletModel
from app_vehicle.models import VehicleModel, DriverModel

def index(request):
    OutletObject = OutletModel.objects.exclude(OutletType='Source')
    VehicleObject = VehicleModel.objects.all()
    DriverObject = DriverModel.objects.all()
    context = {
        'OutletObject' : OutletObject,
        'VehicleObject' : VehicleObject,
        'DriverObject' : DriverObject,
    }
    return render(request, 'dashboard/index.html', context)
# Create your views here.
class Dashboard(View):
    template_name = 'dashboard/index.html'
    
    def get(self, request):
        OutletObject = OutletModel.objects.exclude(OutletType='Source')
        VehicleObject = VehicleModel.objects.all()
        DriverObject = DriverModel.objects.all()
        context = {
            'OutletObject' : OutletObject,
            'VehicleObject' : VehicleObject,
            'DriverObject' : DriverObject,
        }
        return render(request, self.template_name, context)

