from django.shortcuts import render
from app_outlet.models import OutletModel
from .form import ScheduleForm

# Create your views here.
def index(request):
    # OutletObject = OutletModel.objects.all()
    form = ScheduleForm(request.POST or None)
    error=None
    if request.method=='POST':
        if form.is_valid():
            selectedData = form.cleadned_data['data']
            print(selectedData)
        else:
            error = form.errors
    context={
        # 'objectdatas' : OutletObject,
        'form' : form
    }
    return render(request, 'schedule/index.html', context)

def overview(request):
    return render(request, 'schedule/overview.html')

def vehicle(request):
    return render(request, 'schedule/vehicle.html')

def result(request):
    return render(request, 'schedule/result.html')