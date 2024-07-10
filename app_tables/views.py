from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import VehicleModel
from .form import VehicleForm
from .form import DriverForm

# Create your views here.
def outlet_index(request):
    context={
        'PageHeader' : 'Outlet Review',
        'link':'app_tables:outletCreate',
        'linkButton' : 'Add Outlet',
    }
    return render(request, 'tables/outlets/index.html', context)

def outlet_create(request):
    return render(request, 'tables/outlets/create.html')

def outlet_update(request):
    return render(request, 'tables/outlets/update.html')

def outlet_view(request):
    return render(request, 'tables/outlets/view.html')


def vehicle_index(request):
    VehicleObject = VehicleModel.objects.all()
    context={
        'PageHeader' : 'Vehicle & Driver',
        'VehicleLink': 'app_tables:vehicleCreate', 
        'VehicleButton' : 'Add Vehicle',
        'DriverLink' : 'app_tables:driverCreate',
        'DriverButton' : 'Add Driver',
        'Datas' : VehicleObject,
    }
    return render(request, 'tables/vehicles/index.html', context)

def vehicle_create(request):
    Vehicle_Form = VehicleForm(request.POST or None)
    if request.method == 'POST':
        if Vehicle_Form.is_valid():
            Vehicle_Form.save()
            return HttpResponseRedirect('/vehicles/')
    context={
        'form':VehicleForm
    }
    return render(request, 'tables/vehicles/create.html', context)

def vehicle_update(request):
    return render(request, 'tables/vehicles/update.html')

def vehicle_view(request):
    return render(request, 'tables/vehicles/view.html')

def driver_create(request):
    Vehicle_Form = DriverForm(request.POST or None)
    if request.method == 'POST':
        if Vehicle_Form.is_valid():
            Vehicle_Form.save()
            return HttpResponseRedirect('/vehicles/')
    context={
        'form':DriverForm
    }
    return render(request, 'tables/drivers/create.html', context)
