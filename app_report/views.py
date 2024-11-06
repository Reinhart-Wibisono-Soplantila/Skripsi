import os
import json
import pytz
import folium
import polyline
import pandas as pd
from .forms import StatusForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.staticfiles import finders
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app_schedules.models import ScheduleModel, ScheduleOutlet, ScheduleVehicle
from app_vehicle.models import VehicleModel
from app_outlet.models import OutletModel
from app_report.models import Map
from django.db.models import Q
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
def maps(request, Schedule_id):
    
    existing_map = Map.objects.filter(name=Schedule_id).first()
    if existing_map:
        # Jika sudah ada, kembalikan file path atau response sesuai kebutuhan
        return render(request, f'maps/{Schedule_id}.html')
    else:
        VehicleSchedule = ScheduleVehicle.objects.filter(Schedule_id=Schedule_id)
        maps=[]
        for vehicle in VehicleSchedule:
            Route=[]
            key = vehicle.VehicleNumber_id
            OutletObject = ScheduleOutlet.objects.filter(
                Q(Group_vehicle_number=key) & Q(Schedule_id=Schedule_id))
            for iteration in range(len(OutletObject)-1):
                firstKey = OutletObject.values_list('OutletCode', flat=True)[iteration]
                secondKey = OutletObject.values_list('OutletCode', flat=True)[iteration+1]
                Route.append(f'{firstKey}, {secondKey}')
            maps.append(Route)
        
                
        json_file_path = finders.find('files/RouteDetails.json')
        data = {}
        if json_file_path:
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
                
        for map in maps:
            start_route = map[0]
            start_location = [data[start_route]['from']['outlet_coord'][1], data[start_route]['from']['outlet_coord'][0]]
            result_map = folium.Map(location=start_location, zoom_start=12)

            # Loop hanya melalui rute yang dipilih
            
            i=1
            for key in map:
                if key in data:
                    route_data = data[key]
                    from_coord = route_data['from']['outlet_coord']
                    from_coord = [from_coord[1], from_coord[0]]
                    
                    to_coord = route_data['to']['outlet_coord']
                    to_coord = [to_coord[1], to_coord[0]]
                    # Tambahkan marker untuk 'from' dan 'to' outlet
                    # folium.Marker(from_coord, popup=f"From: {route_data['from']['outlet_code']}").add_to(m)
                    # Tambahkan marker hijau untuk semua 'from' outlet
                    folium.Marker(
                        location = from_coord,
                        popup=f"From: {route_data['from']['outlet_code']}, To: {route_data['to']['outlet_code']}",
                        # icon=folium.DivIcon(html=f"""<div style="font-size: 12pt; font-weight: bold; color: black">{i}</div>""")
                    ).add_to(result_map)
                    
                    # folium.Marker(to_coord, popup=f"To: {route_data['to']['outlet_code']}").add_to(m)
                    # Tambahkan marker merah untuk 'to' outlet
                    folium.Marker(
                        location = to_coord,
                        popup=f"From: {route_data['from']['outlet_code']}, To: {route_data['to']['outlet_code']}",
                    ).add_to(result_map)
                    
                    # Decode geometri polyline dan tambahkan ke peta sebagai PolyLine
                    encoded_geometri = route_data['geometri']
                    decoded_coords = polyline.decode(encoded_geometri)
                    
                    # Tambahkan rute ke peta
                    folium.PolyLine(decoded_coords, color="blue", weight=2.5, opacity=1).add_to(result_map)
                i+=1
            
            file_path = os.path.join('app_report', 'templates', 'maps', f'{Schedule_id}.html')
            # Simpan peta ke file HTML
            result_map.save(file_path)
            Map.objects.create(name=Schedule_id, file_path=file_path)
            return render(request, f'maps/{Schedule_id}.html')

@group_required('Admin', 'Driver')
def view(request, Schedule_id):
    VehicleSchedule = ScheduleVehicle.objects.filter(Schedule_id=Schedule_id)
    
    json_file_path = finders.find('files/RouteDetails.json')
    data = {}
    if json_file_path:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            
    RouteListed={}
    for vehicle in VehicleSchedule:
        key = vehicle.VehicleNumber_id
        ScheduleObject = ScheduleOutlet.objects.filter(
            Q(Group_vehicle_number=key) & Q(Schedule_id=Schedule_id))
        vehicleObject = VehicleModel.objects.get(VehicleNumber=key)
        RouteListed[key] = {
            'NumberLocation':vehicle.Total_location_each_vehicle, 
            'detailsVehicle':{
                'ScheduleId' : Schedule_id,
                'VehicleNumber' : vehicleObject.VehicleNumber,
                'VehicleType' : vehicleObject.UnitType,
                'DriverName' : vehicleObject.DriverName,
                'TotalDistance' : vehicle.Total_distance_each_vehicle,
                'TotalOutlets' : vehicle.Total_location_each_vehicle
            }
        }
        if 'detailsRoute' not in RouteListed[key]:
            RouteListed[key]['detailsRoute'] = {}
        for iteration in range(len(ScheduleObject)-1):
            firstKey = ScheduleObject.values_list('OutletCode', flat=True)[iteration]
            secondKey = ScheduleObject.values_list('OutletCode', flat=True)[iteration+1]
            statusRoute = ScheduleObject.values_list('Status', flat=True)[iteration]
            
            firstOutlet = OutletModel.objects.get(OutletCode=firstKey).OutletName
            secondOutlet = OutletModel.objects.get(OutletCode=secondKey).OutletName
            
            searchedKey = f'{firstKey}, {secondKey}'
            FilteredDict = {key: value for key, value in data.items() if key == searchedKey}
            distance = FilteredDict.get(searchedKey, {})
            distance = distance.get('jarak')
            RouteListed[key]['detailsRoute'][searchedKey]={
                'firstOutlet' : firstOutlet,
                'secondOutlet' : secondOutlet,
                'secondCode' : secondKey,
                'distance' : distance,
                'status' : statusRoute
            }
            
    statusForm = StatusForm(request.POST or None)
    error = None
    if request.method == 'POST':
        if statusForm.is_valid():
            selected_outlets_data = request.POST.get("selected-outlets")
            # Parse JSON string menjadi list of dictionaries
            status = statusForm.cleaned_data['Status']
            print(status)
            try:
                selected_outlets = json.loads(selected_outlets_data)
            except json.JSONDecodeError:
                print('error')
            #     return JsonResponse({"error": "Invalid JSON format"}, status=400)
            if not selected_outlets_data:
                print('non')
                # error['selected_outlets'] = "You must select at least one option."
                # messages.error(request, error['selected_outlets'])
            # if not error:
            #     outlets = [str(x) for x in selected_outlets_data.split(',')]
                # request.session['outlets'] = outlets
                # messages.success(request, error['selected_outlets'])
                # return redirect('app_schedules:viewoutlets')
                # return redirect('app_vehicle:vehicleIndex')
        else:
            error = statusForm.errors
            
    context = {
        'RouteListed' : RouteListed,
        'Schedule_id' : Schedule_id,
        'form': statusForm,
        'error':error
    }
    
    # print(RouteListed)
    return render(request, 'report/view.html', context)


@group_required('Admin')
def delete(request, Schedule_id):
    ScheduleObject = ScheduleModel.objects.get(pk=Schedule_id)
    ScheduleObject.delete()
    return redirect('app_report:index')