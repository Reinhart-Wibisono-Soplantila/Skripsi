from django.shortcuts import render, redirect
from app_outlet.models import OutletModel
from app_vehicle.models import VehicleModel, DriverModel
from .algorithm.GA import GeneticAlgorithm 
from .algorithm.SMO import SpiderMonkeyAlgorithm
from django.contrib import messages

# Create your views here.
def index(request):
    # OutletObject = OutletModel.objects.all()
    OutletObject = OutletModel.objects.all()
    error={}
    if request.method == 'POST':
        CheckedList = request.POST.get('selected_outlets', '')
        print(CheckedList)
        if not CheckedList:
            error['selected_outlets'] = "You must select at least one option."
            print('error')
        if not error:
            cities = [str(x) for x in CheckedList.split(',')]
            request.session['cities'] = cities
            messages.success(request, error['selected_outlets'])
            return redirect('app_schedules:viewoutlets')
    context={
        'error' : error,
        'OutletObject' : OutletObject
    }
    return render(request, 'schedule/index.html', context)

def viewoutlets(request):
    # Ambil ID dari sesi
    citiesId = request.session.get('cities', [])
    OutletObject = OutletModel.objects.filter(OutletCode__in=citiesId)
    context={
        'OutletObject' : OutletObject
    }
    return render(request, 'schedule/confirm.html', context)

def processoutlets(request):
    cities = request.session.get('cities', [])
    # GA
    GA = GeneticAlgorithm()
    answer, genNumber  = GA.main(cities)
    # print('answer=', answer[0])
    # print('location=', answer[1])
    # print(genNumber)
    request.session['locations'] = answer[1]
    request.session['distance'] = answer[0]
    
    # SMO
    # SMO = SpiderMonkeyAlgorithm()
    # location, fitness = SMO.main(cities)
    # request.session['locations'] = location
    # request.session['distance'] = fitness
            
    # Hapus data dari sesi jika tidak diperlukan lagi
    # request.session.pop('cities_ids', None)
    return redirect('app_schedules:vehicles')
    # return render( request, 'schedule/selectedOutlets.html')
    
def vehicles(request):
    VehicleObject = VehicleModel.objects.all()
    error = {}
    if request.method == 'POST':
        
        CheckedList = request.POST.get('selected_vehicles', '')
        # CheckedList = request.POST.get('datas', '')
        if not CheckedList:
            error['selected_vehicles'] = "You must select at least one option."
            print('error')
        if not error:
            Vehicles = [str(x) for x in CheckedList.split(',')]
            request.session['vehicles'] = Vehicles
            return redirect('app_schedules:drivers')
    context={
        'VehicleObject' : VehicleObject,
    }
    return render(request, 'schedule/vehicle.html', context)

def drivers(request):
    DriverObject = DriverModel.objects.all()
    error = {}
    if request.method == 'POST':
        
        CheckedList = request.POST.get('selected_drivers', '')
        # CheckedList = request.POST.get('datas', '')
        if not CheckedList:
            error['selected_drivers'] = "You must select at least one option."
            print('error')
        if not error:
            print('check :',CheckedList)
            # Vehicles = [str(x) for x in CheckedList.split(',')]
            # request.session['selected_drivers'] = Vehicles
            return redirect('app_schedules:drivers')
    context={
        'DriverObject' : DriverObject,
    }
    return render(request, 'schedule/driver.html', context)

def overview(request):
    return render(request, 'schedule/overview.html')


def result(request):
    return render(request, 'schedule/result.html')