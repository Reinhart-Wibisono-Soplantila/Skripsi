from django.shortcuts import render, get_object_or_404, redirect
from .models import OutletModel
from .form import OutletForm

# Create your views here.
# Outlet Views
def outlet_index(request):
    OutletObject = OutletModel.objects.all()
    context={
        'PageHeader' : 'Outlet Review',
        'link':'app_outlet:outletCreate',
        'linkButton' : 'Add Outlet',
        'OutletDatas' : OutletObject
    }
    return render(request, 'outlet/index.html', context)

def outlet_create(request):
    OutletForm_Create = OutletForm(request.POST or None)
    error = None
    if request.method == 'POST':
        print(request.POST)
        if OutletForm_Create.is_valid():
            OutletForm_Create.save()
            return redirect('app_outlet:outletIndex')
        else:
            error = OutletForm_Create.errors
    context={
        'pageHeader' : 'Add Outlet',
        'form' : OutletForm,
        'error' : error
    }
    return render(request, 'outlet/create.html', context)

def outlet_update(request, outletCode):
    updated_data = get_object_or_404(OutletModel, OutletCode = outletCode)
    OutletForm_updated = OutletForm(request.POST or None, instance=updated_data)
    error = None
    if request.method == 'POST':
        if OutletForm_updated.is_valid():
            OutletForm_updated.save()
            return redirect('app_outlet:outletIndex')
    else:
        error= OutletForm_updated.errors
    context = {
        'pageHeader' : 'Update Outlet',
        'form' : OutletForm_updated,
        'error' : error,
    }
    return render(request, 'outlet/update.html', context)

def outlet_view(request, outletCode):
    selected_data = get_object_or_404(OutletModel, OutletCode = outletCode)
    OutletForm_selected = OutletForm(instance=selected_data)
    for field in OutletForm_selected.fields.values():
        field.widget.attrs['disabled'] = 'disabled'
    
    context = {
        'pageHeader' : 'View Outlet',
        'form' : OutletForm_selected
    }
    return render(request, 'outlet/view.html', context)


def outlet_delete(request, outletCode):
    OutletModel.objects.filter(OutletCode=outletCode).delete()
    return redirect('app_outlet:outletIndex')

# # Loations Views
# def load_regencies(request):
#     province_id = request.GET.get('Provinsi')
#     regencies = reg_Regencies.objects.filter(province_id=province_id).order_by('name')
#     return JsonResponse(list(regencies.values('id', 'name')), safe=False)

# def load_districts(request):
#     regency_id = request.GET.get('Kabupaten')
#     districts = reg_Districts.objects.filter(regency_id=regency_id).order_by('name')
#     return JsonResponse(list(districts.values('id', 'name')), safe=False)

# def load_villages(request):
#     district_id = request.GET.get('Kecamatan')
#     villages = reg_Villages.objects.filter(district_id=district_id).order_by('name')
#     return JsonResponse(list(villages.values('id', 'name')), safe=False)