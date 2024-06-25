from django.shortcuts import render
from django.http import HttpResponseRedirect
from .formVehicle import VehicleForm

# Create your views here.
def outlets_index(request):
    context={
        'link':'datatables:outletCreate',
        'linkButton' : 'Add Outlet',
    }
    return render(request, 'tables/index.html', context)

def outlets_create(request):
    return render(request, 'tables/outlets/create.html')

def outlets_update(request):
    return render(request, 'tables/outlets/update.html')

def outlets_view(request):
    return render(request, 'tables/outlets/view.html')


def vehicles_index(request):
    context={
        'link':'datatables:vehicleCreate', 
        'linkButton' : 'Add Vehicle',
    }
    return render(request, 'tables/index.html', context)

def vehicles_create(request):
    Vehicle_Form = VehicleForm(request.POST or None)
    if request.method == 'POST':
        if Vehicle_Form.is_valid():
            Vehicle_Form.save()
            return HttpResponseRedirect('/vehicles/')
    context={
        'form':VehicleForm
    }
    return render(request, 'tables/vehicles/create.html', context)

def vehicles_update(request):
    return render(request, 'tables/vehicles/update.html')

def vehicles_view(request):
    return render(request, 'tables/vehicles/view.html')