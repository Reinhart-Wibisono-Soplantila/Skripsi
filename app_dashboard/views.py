import json
from django.shortcuts import render
from django.views.generic import View
from app_outlet.models import OutletModel
from app_schedules.models import ScheduleModel
from app_vehicle.models import VehicleModel, DriverModel
from datetime import datetime, timedelta

def index(request):
    
    # Mengambil tanggal dan jam hari ini
    today = datetime.today()
    
    # Mencari tanggal pada hari senin minggu ini
    monday_this_week = today - timedelta(days=today.weekday())
    print('monday_this_week: ', monday_this_week)
    # MEncari tanggal pada hari senin dan sabtu minggu sebelumnya
    monday_last_week = monday_this_week - timedelta(weeks=1)
    sunday_last_week = monday_last_week + timedelta(days=6)
    print('monday_last_week:', monday_last_week)
    # first_day_last_month = today.replace(day=1) - timedelta(days=1)
    # first_day_last_month = first_day_last_month.replace(day=1)
    
    # Ambil data pengiriman dan jumlah toko untuk tiap rentang waktu
    # minggu ini
    shipments_this_week = ScheduleModel.objects.filter(Created_at__gte=monday_this_week).values('Schedule_id', 'Created_at')
    shipments_last_week = ScheduleModel.objects.filter(Created_at__gte=monday_last_week, Created_at__lt=sunday_last_week).values('Schedule_id', 'Created_at')
    
    
    # List nama hari dari Senin hingga Sabtu
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # Membuat dictionary dengan key berupa nama hari
    schedule_by_day_this_week = {day: {'Count': 0} for day in day_names}
    schedule_by_day_last_week = {day: {'Count': 0} for day in day_names}
    
    # Isi dictionary dengan data yang ditemukan
    for current_shipment in shipments_this_week:
        day_name = current_shipment['Created_at'].strftime('%A')
        if day_name in schedule_by_day_this_week:
            schedule_id = current_shipment['Schedule_id']
            schedule_object = ScheduleModel.objects.get(Schedule_id=schedule_id).Destination_outlet.all()
            outlet_count = schedule_object.count()
            # Simpan informasi dalam dictionary per hari
            schedule_by_day_this_week[day_name] = {
                'count': outlet_count
            }
    for last_shipment in shipments_last_week:
        day_name = last_shipment['Created_at'].strftime('%A')
        if day_name in schedule_by_day_last_week:
            schedule_id = last_shipment['Schedule_id']
            schedule_object = ScheduleModel.objects.get(Schedule_id=schedule_id).Destination_outlet.all()
            outlet_count = schedule_object.count()
            # Simpan informasi dalam dictionary per hari
            schedule_by_day_last_week[day_name] = {
                'count': outlet_count
            }
            
    for day, scheduleData in schedule_by_day_last_week.items():
        print(f"{day}: {scheduleData}")
    context = {
        'schedule_by_day_this_week_json': json.dumps(schedule_by_day_this_week),  # Convert to JSON
        'schedule_by_day_this_last_json': json.dumps(schedule_by_day_last_week)  # Convert to JSON
    }
    return render(request, 'dashboard/index.html', context)
# Create your views here.
class Dashboard(View):
    template_name = 'dashboard/index.html'
    
    def get(self, request):
        OutletObject = OutletModel.objects.exclude(OutletType='Source')
        VehicleObject = VehicleModel.objects.all()
        DriverObject = DriverModel.objects.all()
        
        today = datetime.today()
        monday_this_week = today - timedelta(days=today.weekday())  # Mulai Senin minggu ini
        # monday_last_week = monday_this_week - timedelta(weeks=1)
        print('today: ', today)
        print('monday_this_week : ', monday_this_week)
        # first_day_last_month = today.replace(day=1) - timedelta(days=1)
        # first_day_last_month = first_day_last_month.replace(day=1)
        
        # Ambil data pengiriman dan jumlah toko untuk tiap rentang waktu
        ScheduleObject = ScheduleModel.objects.all()
        shipments_this_week = ScheduleObject.objects.filter(date__gte=monday_this_week).values_list('Schedule_id', flat=True)
        print('shipments_this_week : ',shipments_this_week)
        # shipments_last_week = ScheduleObject.Destination_outlet.objects.filter(date__gte=monday_last_week, date__lt=monday_this_week).values('date').annotate(count=Count('store'))
        # shipments_last_month = ScheduleObject.Destination_outlet.objects.filter(date__gte=first_day_last_month, date__lt=first_day_last_month + timedelta(days=30)).values('date').annotate(count=Count('store'))

        # Format data sesuai kebutuhan untuk ditampilkan di Chart.js
        labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        this_week_data = [0, 0, 0, 0, 0, 0]  # Placeholder untuk data minggu ini
        last_week_data = [0, 0, 0, 0, 0, 0]  # Placeholder untuk data minggu lalu
        last_month_data = [0, 0, 0, 0, 0, 0]  # Placeholder untuk data bulan lalu
    
        context = {
            'OutletObject' : OutletObject,
            'VehicleObject' : VehicleObject,
            'DriverObject' : DriverObject,
        }
        return render(request, self.template_name, context)

