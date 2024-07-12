from django.shortcuts import render, get_object_or_404, redirect
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
    VehicleForm_Create = VehicleForm(request.POST or None)
    error = None
    if request.method == 'POST':
        if VehicleForm_Create.is_valid():
            VehicleForm_Create.save()
            return redirect('app_tables:vehicleIndex')
        else:
            error = VehicleForm_Create.errors
    context={
        'form': VehicleForm,
        'error' : error 
    }
    return render(request, 'tables/vehicles/create.html', context)

def vehicle_update(request, vehicleNumber):
    updated_data = get_object_or_404(VehicleModel, VehicleNumber=vehicleNumber)
    VehicleForm_updated = VehicleForm(request.POST or None, instance=updated_data)
    error = None
    if(request.method == 'POST'):
        if(VehicleForm_updated.is_valid()):
            VehicleForm_updated.save()
            return redirect('app_tables:vehicleIndex')
        else:
            error = VehicleForm_updated.errors
    context={
        'form':VehicleForm_updated,
        'error':error
    }
    return render(request, 'tables/vehicles/update.html', context)

def vehicle_delete(request, vehicleNumber):
    VehicleModel.objects.filter(VehicleNumber = vehicleNumber).delete()
    return redirect('app_tables:vehicleIndex')

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
