from django.shortcuts import render, redirect
from app_outlet.models import OutletModel
from .algorithm.GA import GeneticAlgorithm 

# Create your views here.
def index(request):
    # OutletObject = OutletModel.objects.all()
    OutletObject = OutletModel.objects.all()
    error={}
    if request.method == 'POST':
        CheckedList = request.POST.get('datas', '')
        if not CheckedList:
            error['datas'] = "You must select at least one option."
            print('error')
        if not error:
            cities = [str(x) for x in CheckedList.split(',')]
            request.session['cities'] = cities
            return redirect('app_schedules:viewoutlets')
    context={
        'error' : error,
        'OutletObject' : OutletObject
    }
    return render(request, 'schedule/index.html', context)

def viewoutlets(request):
    error={}
    # Ambil ID dari sesi
    citiesId = request.session.get('cities', [])
    OutletObject = OutletModel.objects.filter(OutletCode__in=citiesId)
    context={
        'error' : error,
        'OutletObject' : OutletObject
    }
    return render(request, 'schedule/selectedOutlets.html', context)

def processoutlets(request):
    cities = request.session.get('cities', [])
    print('cities', cities)
    GA = GeneticAlgorithm()
    answer, genNumber  = GA.main(cities)
    print('answer=', answer[0])
    print('location=', answer[1])
    print(genNumber)
            
    # Hapus data dari sesi jika tidak diperlukan lagi
    request.session.pop('cities_ids', None)
    request.session['locations'] = answer[1]
    request.session['distance'] = answer[0]
    return redirect('app_schedules:viewoutlets')
    # return render( request, 'schedule/selectedOutlets.html')
def overview(request):
    return render(request, 'schedule/overview.html')

def vehicle(request):
    return render(request, 'schedule/vehicle.html')

def result(request):
    return render(request, 'schedule/result.html')