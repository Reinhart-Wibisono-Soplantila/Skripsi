from django.shortcuts import render, redirect
from app_outlet.models import OutletModel
from .form import ScheduleForm

# Create your views here.
def index(request):
    # OutletObject = OutletModel.objects.all()
    form = ScheduleForm(request.POST or None)
    error=None
    if request.method == 'POST':
        print("Request Method is POST")
        print("POST Data:", request.POST)
        if form.is_valid():
            print("Form is valid")
            selectedData = form.cleaned_data['datas']
            print(selectedData)
            redirect ('app_schedules:index')
        else:
            print("Form is not valid")
            error = form.errors
            print(error)
    context={
        # 'objectdatas' : OutletObject,
        'form' : form,
        'error' : error,
    }
    return render(request, 'schedule/index.html', context)

def overview(request):
    return render(request, 'schedule/overview.html')

def vehicle(request):
    return render(request, 'schedule/vehicle.html')

def result(request):
    return render(request, 'schedule/result.html')