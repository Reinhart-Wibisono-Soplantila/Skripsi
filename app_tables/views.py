from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import VehicleModel, DriverModel, OutletModel
from .models import reg_Provinces, reg_Regencies, reg_Districts, reg_Villages
from .form import VehicleForm, DriverForm, OutletForm, OutletViewForm

# Create your views here.
# Outlet Views
def outlet_index(request):
    OutletObject = OutletModel.objects.all()
    context={
        'PageHeader' : 'Outlet Review',
        'link':'app_tables:outletCreate',
        'linkButton' : 'Add Outlet',
        'OutletDatas' : OutletObject
    }
    return render(request, 'tables/outlets/index.html', context)

def outlet_create(request):
    OutletForm_Create = OutletForm(request.POST or None)
    error = None
    if request.method == 'POST':
        print(request.POST)
        if OutletForm_Create.is_valid():
            OutletForm_Create.save()
            return redirect('app_tables:outletIndex')
        else:
            error = OutletForm_Create.errors
    context={
        'pageHeader' : 'Add Outlet',
        'form' : OutletForm,
        'error' : error
    }
    return render(request, 'tables/outlets/create.html', context)

def outlet_update(request, outletCode):
    updated_data = get_object_or_404(OutletModel, OutletCode = outletCode)
    # OutletForm_updated = OutletForm(request.POST or None, instance=updated_data)
    error = None
    if request.method == 'POST':
        form = OutletForm(request.POST, instance=updated_data)
        if form.is_valid():
            form.save()
            return redirect('nama_view_atau_url_yang_diinginkan')
    else:
        form = OutletForm(instance=updated_data)
    context = {
        'pageHeader' : 'Update Outlet',
        'form' : form,
        'error' : error,
    }
    return render(request, 'tables/outlets/update.html', context)

def outlet_view(request, outletCode):
    selected_data = get_object_or_404(OutletModel, OutletCode = outletCode)
    OutletForm_selected = OutletViewForm(instance=selected_data)
    for field in OutletForm_selected.fields.values():
        field.widget.attrs['disabled'] = 'disabled'
    
    context = {
        'pageHeader' : 'View Outlet',
        'form' : OutletForm_selected
    }
    return render(request, 'tables/outlets/view.html', context)


def outlet_delete(request, outletCode):
    OutletModel.objects.filter(OutletCode=outletCode).delete()
    return redirect('app_tables:outletIndex')

# Loations Views
def load_regencies(request):
    province_id = request.GET.get('Provinsi')
    regencies = reg_Regencies.objects.filter(province_id=province_id).order_by('name')
    return JsonResponse(list(regencies.values('id', 'name')), safe=False)

def load_districts(request):
    regency_id = request.GET.get('Kabupaten')
    districts = reg_Districts.objects.filter(regency_id=regency_id).order_by('name')
    return JsonResponse(list(districts.values('id', 'name')), safe=False)

def load_villages(request):
    district_id = request.GET.get('Kecamatan')
    villages = reg_Villages.objects.filter(district_id=district_id).order_by('name')
    return JsonResponse(list(villages.values('id', 'name')), safe=False)


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

def driver_delete(request, driverId):
    DriverModel.objects.filter(id=driverId).delete()
    return redirect('app_tables:vehicleIndex')