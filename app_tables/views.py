from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import VehicleModel, DriverModel
from .form import VehicleForm, DriverForm

# Create your views here.
# outlet views
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

# vehicle views
def vehicle_index(request):
    VehicleObject = VehicleModel.objects.all()
    DriverObject = DriverModel.objects.all()
    context={
        'PageHeader' : 'Vehicle & Driver',
        'VehicleLink': 'app_tables:vehicleCreate', 
        'VehicleButton' : 'Add Vehicle',
        'DriverLink' : 'app_tables:driverCreate',
        'DriverButton' : 'Add Driver',
        'VehicleDatas' : VehicleObject,
        'DriverDatas' : DriverObject,
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
        'pageHeader' : 'Add Vehicle',
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
        'pageHeader' : 'Vehicle Update',
        'form':VehicleForm_updated,
        'error':error
    }
    return render(request, 'tables/vehicles/update.html', context)

def vehicle_delete(request, vehicleNumber):
    VehicleModel.objects.filter(VehicleNumber = vehicleNumber).delete()
    return redirect('app_tables:vehicleIndex')

# driver views
def driver_create(request):
    DriverForm_Create = DriverForm(request.POST or None)
    error = None
    if request.method == 'POST':
        if DriverForm_Create.is_valid():
            DriverForm_Create.save()
            return redirect('app_tables:vehicleIndex')
        else:
            # print(DriverForm_Create.errors)
            error = DriverForm_Create.errors
    context={
        'pageHeader' : 'Add Driver',
        'form' : DriverForm,
        'error' : error
    }
    return render(request, 'tables/drivers/create.html', context)

def driver_update(request, driverId):
    updated_data = get_object_or_404(DriverModel, id=driverId)
    DriverForm_updated = DriverForm(request.POST or None, instance=updated_data)
    error = None
    if(request.method == 'POST'):
        if(DriverForm_updated.is_valid()):
            DriverForm_updated.save()
            return redirect('app_tables:vehicleIndex')
        else:
            error = DriverForm_updated.errors
    context={
        'pageHeader' : 'Driver Update',
        'form':DriverForm_updated,
        'error':error
    }
    return render(request, 'tables/drivers/update.html', context)

def driver_delete(request, driverId):
    DriverModel.objects.filter(id=driverId).delete()
    return redirect('app_tables:vehicleIndex')

def driver_view(request, driverId):
    selected_data = get_object_or_404(DriverModel, id=driverId)
    DriverForm_selected = DriverForm(instance=selected_data)
    
    for field in DriverForm_selected.fields.values():
        field.widget.attrs['disabled'] = 'disabled'
    
    context = {
        'pageHeader' : 'View Driver',
        'form' : DriverForm_selected
    }
    return render(request, 'tables/drivers/view.html', context)