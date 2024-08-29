import json
from django.shortcuts import render, redirect
from django.db.models import Case, When
from django.contrib.staticfiles import finders
from django.contrib import messages
from app_outlet.models import OutletModel
from app_schedules.models import ScheduleModel
from app_vehicle.models import VehicleModel, DriverModel
from .algorithm.GA import GeneticAlgorithm 
from .algorithm.SMO import SpiderMonkeyAlgorithm
from django.utils import timezone
from datetime import datetime

# Create your views here.
def index(request):
    # OutletObject = OutletModel.objects.all()
    OutletObject = OutletModel.objects.exclude(OutletType='Source')
    error={}
    
    if request.method == 'POST':
        CheckedList = request.POST.get('selected_outlets', '')
        
        if not CheckedList:
            error['selected_outlets'] = "You must select at least one option."
            messages.error(request, error['selected_outlets'])
        if not error:
            outlets = [str(x) for x in CheckedList.split(',')]
            request.session['outlets'] = outlets
            # messages.success(request, error['selected_outlets'])
            return redirect('app_schedules:viewoutlets')
        
    context={
        'error' : error,
        'OutletObject' : OutletObject
    }
    request.session.pop('locations', None)
    request.session.pop('distance', None)
    request.session.pop('drivers', None)
    request.session.pop('vehicles', None)
    return render(request, 'schedule/index.html', context)

def viewoutlets(request):
    # Ambil ID dari sesi
    citiesId = request.session.get('outlets', [])
    OutletObject = OutletModel.objects.filter(OutletCode__in=citiesId)
    context={
        'OutletObject' : OutletObject
    }
    print(OutletObject)
    return render(request, 'schedule/confirm.html', context)

def processoutlets(request):
    outlets = request.session.get('outlets', [])
    # GA
    GA = GeneticAlgorithm()
    answer, genNumber  = GA.main(outlets)
    answer[1].insert(0, '15000000000000000000000000')
    
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
            messages.error(request, error['selected_vehicles'])
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
            messages.error(request, error['selected_drivers'])
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
    locations = request.session.get('locations', [])
    distance = request.session.get('distance', [])
    drivers = request.session.get('drivers', [])
    vehicles = request.session.get('vehicles', [])
    OutletObject = OutletModel.objects.filter(OutletCode__in=locations).order_by(
        Case(*[When(OutletCode=id, then=pos) for pos, id in enumerate(locations)])
        )
    VehicleObject = VehicleModel.objects.filter(id__in=vehicles)
    DriverObject = DriverModel.objects.filter(id__in=drivers)
    print('location:', locations)
    # print('distance:', distance)
    print('drivers:', DriverObject)
    print('vehicles:', VehicleObject)
    # print('locations:', OutletObject)
    
    # Find the path to the JSON file
    json_file_path = finders.find('files/RouteDetails.json')
    data = {}
    if json_file_path:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
    
    RouteListed={}
    # print(OutletObject[0])
    for iteration in range(len(OutletObject)-1):
        firstKey = OutletObject.values_list('OutletCode', flat=True)[iteration]
        secondKey = OutletObject.values_list('OutletCode', flat=True)[iteration+1]
        searchedKey = f'{firstKey}, {secondKey}'
        FilteredDict = {key: value for key, value in data.items() if key == searchedKey}
        RouteListed[searchedKey] = FilteredDict[searchedKey]
        # RouteListed.append(FilteredDict)
    RouteListed_length = len(RouteListed)
    
    if request.method == 'POST':
        schedule = ScheduleModel(Distance=distance)
        schedule.save()
        
        for outlet in OutletObject:
            schedule.Destination_outlet.add(outlet)
        schedule.Vehicle_used.add(*VehicleObject)
        schedule.Driver_used.add(*DriverObject)
        
        for vehicle in VehicleObject:
            vehicle.Status = 'Used'  # Perbarui status kendaraan menjadi 'used'
            vehicle.Used_at = timezone.now()
            vehicle.save()  # Simpan perubahan status
        
        request.session.pop('outlet_ids', None)
        request.session.pop('driver_ids', None)
        request.session.pop('vehicle_ids', None)
        return redirect('app_schedules:index')
        
    context ={
        'OutletObject' : OutletObject,
        'distance' : distance,
        'DriverObject' : DriverObject,
        'VehicleObject' : VehicleObject,
        'RouteListed' : RouteListed,
        'TotalLocation' : RouteListed_length
    }
    return redirect('app_report:index')