from django.shortcuts import render, redirect
from app_outlet.models import OutletModel
from app_vehicle.models import VehicleModel, DriverModel
from .algorithm.GA import GeneticAlgorithm 
from .algorithm.SMO import SpiderMonkeyAlgorithm

# Create your views here.
def index(request):
    # OutletObject = OutletModel.objects.all()
    OutletObject = OutletModel.objects.all()
    error={}
    if request.method == 'POST':
        CheckedList = request.POST.get('selected_outlets', '')
        
        if not CheckedList:
            error['selected_outlets'] = "You must select at least one option."
            print('error')
        if not error:
            outlets = [str(x) for x in CheckedList.split(',')]
            request.session['outlets'] = outlets
            # messages.success(request, error['selected_outlets'])
            return redirect('app_schedules:viewoutlets')
    context={
        'error' : error,
        'OutletObject' : OutletObject
    }
    return render(request, 'schedule/index.html', context)

def viewoutlets(request):
    # Ambil ID dari sesi
    citiesId = request.session.get('outlets', [])
    OutletObject = OutletModel.objects.filter(OutletCode__in=citiesId)
    context={
        'OutletObject' : OutletObject
    }
    return render(request, 'schedule/confirm.html', context)

def processoutlets(request):
    outlets = request.session.get('outlets', [])
    # GA
    GA = GeneticAlgorithm()
    answer, genNumber  = GA.main(outlets)
    print('answer=', answer[0])
    print('location=', answer[1])
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

def vehicles(request):
    VehicleObject = VehicleModel.objects.all()
    error = {}
    if request.method == 'POST':
        
        CheckedList = request.POST.get('selected_vehicles', '')
        if not CheckedList:
            error['selected_vehicles'] = "You must select at least one option."
            print("ERRRRROOOOOORRRRR")
        if not error:
            print('check: ',CheckedList)
            Vehicles = [int(x) for x in CheckedList.split(',')]
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
            print('check:', CheckedList)
            Drivers = [int(x) for x in CheckedList.split(',')]
            request.session['drivers'] = Drivers
            return redirect('app_schedules:result')
    context={
        'DriverObject' : DriverObject,
    }
    return render(request, 'schedule/driver.html', context)

def result(request):
    location = request.session.get('locations', [])
    distance = request.session.get('distance', [])
    drivers = request.session.get('drivers', [])
    vehicles = request.session.get('vehicles', [])
    vehiclesObj = VehicleModel.objects.filter(id__in=vehicles)
    driversObj = DriverModel.objects.filter(id__in=drivers)
    print('location:', location)
    print('distance:', distance)
    # print('drivers:', driversObj)
    # print('vehicles:', vehiclesObj)
    
    
    return render(request, 'schedule/result.html')