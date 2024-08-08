import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.staticfiles import finders
from app_schedules.models import ScheduleModel

# Create your views here.
def index(request):
    ScheduleObject = ScheduleModel.objects.all()
    context = {
        'ScheduleObject' : ScheduleObject,
    }
    return render(request, 'report/index.html', context)

def view(request, Schedule_id):
    ScheduleObject = get_object_or_404(ScheduleModel, Schedule_id=Schedule_id)
    OutletObject = ScheduleObject.Destination_outlet.all()
    TotalLocation = len(OutletObject)
    # Find the path to the JSON file
    json_file_path = finders.find('files/RouteDetails.json')
    data = {}
    if json_file_path:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
    
    RouteListed={}
    for iteration in range(len(OutletObject)-1):
        firstKey = OutletObject.values_list('OutletCode', flat=True)[iteration]
        secondKey = OutletObject.values_list('OutletCode', flat=True)[iteration+1]
        searchedKey = f'{firstKey}, {secondKey}'
        FilteredDict = {key: value for key, value in data.items() if key == searchedKey}
        RouteListed[searchedKey] = FilteredDict[searchedKey]
    
    context = {
        'ScheduleObject' : ScheduleObject,
        'RouteListed' : RouteListed,
        'TotalLocation' : TotalLocation,
    }
    return render(request, 'report/view.html', context)

def delete(request, Schedule_id):
    ScheduleObject = ScheduleModel.objects.get(pk=Schedule_id)

    # Menghapus semua relasi ManyToMany terkait secara manual sebelum menghapus instance
    ScheduleObject.Destination_outlet.clear()
    ScheduleObject.Vehicle_used.clear()
    ScheduleObject.Driver_used.clear()
    
    ScheduleObject.delete()
    return redirect('app_report:index')