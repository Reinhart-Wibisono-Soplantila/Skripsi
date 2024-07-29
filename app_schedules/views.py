from django.shortcuts import render, redirect
from app_outlet.models import OutletModel
from .algorithm.GA import GeneticAlgorithm 

# Create your views here.
def index(request):
    # OutletObject = OutletModel.objects.all()
    Outletdatas = OutletModel.objects.all()
    error={}
    if request.method == 'POST':
        CheckedList = request.POST.get('datas', '')
        if not CheckedList:
            error['datas'] = "You must select at least one option."
            print('error')
            
        if not error:
            cities = [str(x) for x in CheckedList.split(',')]
            request.session['cities'] = cities
            # # print('form is valid')
            # # print("POST Data:", CheckedList)
            # # print('')
            # # print('populasi :', cities)
            # # print('')
            # GA = GeneticAlgorithm()
            # answer, genNumber  = GA.main(cities)
            # print('answer=', answer[0])
            # print('location=', answer[1])
            # print(genNumber)
            # redirect('app_schedules:viewoutlets')
    context={
        'error' : error,
        'OutletObject' : Outletdatas
    }
    return render(request, 'schedule/index.html', context)

def viewoutlets(request):
    error={}
    # Ambil ID dari sesi
    citiesId = request.session.get('cities', [])
    
    # Ambil data dari database berdasarkan ID
    data = OutletModel.objects.filter(id__in=citiesId)
    context={
        'error' : error,
        'data' : data
    }
    return render(request, 'schedule/index.html'. context)

def processoutlets(request):
        
    # Hapus data dari sesi jika tidak diperlukan lagi
    request.session.pop('cities_ids', None)
    
    # GA = GeneticAlgorithm()
    # answer, genNumber  = GA.main(cities)
    # print('answer=', answer[0])
    # print('location=', answer[1])
    # print(genNumber)
    # redirect('app_schedules:viewoutlets')
def overview(request):
    return render(request, 'schedule/overview.html')

def vehicle(request):
    return render(request, 'schedule/vehicle.html')

def result(request):
    return render(request, 'schedule/result.html')