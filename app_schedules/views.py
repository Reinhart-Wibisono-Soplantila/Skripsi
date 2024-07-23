from django.shortcuts import render
from app_outlet.models import OutletModel

# Create your views here.
def index(request):
    OutletObject = OutletModel.objects.all()
    context={
        'objectdatas' : OutletObject,
    }
    return render(request, 'schedule/index.html', context)

def overview(request):
    return render(request, 'schedule/overview.html')

def vehicle(request):
    return render(request, 'schedule/vehicle.html')

def result(request):
    return render(request, 'schedule/result.html')