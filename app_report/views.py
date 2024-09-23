import json
import pytz
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.staticfiles import finders
from app_schedules.models import ScheduleModel
from app_outlet.models import OutletModel
from django.utils import timezone
from django.utils.timezone import make_naive
from proweb.decorators import group_required

# Create your views here.
@group_required('Admin', 'Driver')
def index(request):
    ScheduleObject = ScheduleModel.objects.all()
    # Konversi waktu UTC ke zona waktu lokal pengguna
    display_timezone = pytz.timezone('Asia/Makassar')
    for item in ScheduleObject:
        print(f"UTC Time: {item.Created_at}, Local Time: {item.Created_at.astimezone(display_timezone)}")
        
        # item.Created_at = item.Created_at.astimezone(display_timezone)
        item.Created_at = make_naive(item.Created_at, display_timezone)
        print(item.Created_at)
    print('')
    for item in ScheduleObject:
        print(item.Created_at)
    context = {
        'ScheduleObject' : ScheduleObject,
    }
    print(context)
    return render(request, 'report/index.html', context)

@group_required('Admin', 'Driver')
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
        dist = FilteredDict.get(searchedKey, {})
        dist = dist.get('jarak')
        firstOutlet = OutletModel.objects.get(OutletCode=firstKey).OutletName
        secondOutlet = OutletModel.objects.get(OutletCode=secondKey).OutletName
        RouteListed[searchedKey] = {
            'distance' : dist,
            'firstOutlet' : firstOutlet,
            'secondOutlet' : secondOutlet
            }

    for key in RouteListed:
        print(f"{RouteListed[key]}")
    context = {
        'ScheduleObject' : ScheduleObject,
        'RouteListed' : RouteListed,
        'TotalLocation' : TotalLocation,
    }
    return render(request, 'report/view.html', context)

@group_required('Admin')
def delete(request, Schedule_id):
    ScheduleObject = ScheduleModel.objects.get(pk=Schedule_id)
    ScheduleObject.delete()
    return redirect('app_report:index')