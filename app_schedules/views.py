from django.shortcuts import render, redirect
from app_outlet.models import OutletModel
# from .form import ScheduleForm

# Create your views here.
def index(request):
    # OutletObject = OutletModel.objects.all()
    Outletdatas = OutletModel.objects.all()
    error={}
    if request.method == 'POST':
        print("Request Method is POST")
        print("POST Data:", request.POST)
        print('')
        
        CheckedList = request.POST.getlist('datas') 
        # if form.is_valid():
        #     print("Form is valid")
        #     selectedData = form.cleaned_data['datas']
        #     print(selectedData)
        #     print('')
        #     # Mengambil semua ID dari objek yang dipilih
        #     # selected_ids = [outlet.OutletCode for outlet in selectedData]
            
        #     # # Menampilkan ID untuk tujuan debug
        #     # print("Selected IDs:", selected_ids)
            
        #     redirect ('app_schedules:index')
        # else:
        #     print("Form is not valid")
        #     error = form.errors
        #     print(error)
        if not CheckedList:
            error['datas'] = "You must select at least one option."

        if not error:
            print('form is valid')
            print("POST Data:", CheckedList)
            # return redirect('success')
    context={
        # 'objectdatas' : OutletObject,
        # 'form' : form,
        'error' : error,
        'OutletObject' : Outletdatas
    }
    return render(request, 'schedule/index.html', context)

def overview(request):
    return render(request, 'schedule/overview.html')

def vehicle(request):
    return render(request, 'schedule/vehicle.html')

def result(request):
    return render(request, 'schedule/result.html')