from django.shortcuts import render, redirect
from app_outlet.models import OutletModel
from .algorithm.GeneticAlgorithm import main

# Create your views here.
def index(request):
    # OutletObject = OutletModel.objects.all()
    Outletdatas = OutletModel.objects.all()
    error={}
    if request.method == 'POST':
        print("Request Method is POST")
        print("POST Data:", request.POST)
        print('')
        
        CheckedList = request.POST.get('datas', '')
        if not CheckedList:
            error['datas'] = "You must select at least one option."
            print('error')

        if not error:
            population = [int(x) for x in CheckedList.split(',')]
            print('form is valid')
            print("POST Data:", CheckedList)
            print('')
            print('populasi :', population)
            
            best_individual = main(population)
            print(best_individual)
    context={
        # 'objectdatas' : OutletObject,
        # 'form' : form,
        'error' : error,
        'OutletObject' : Outletdatas
    }
    return render(request, 'schedule/index.html', context)

def overview(request):
    return render(request, 'schedule/overview.html')

def vehicle(request):
    return render(request, 'schedule/vehicle.html')

def result(request):
    return render(request, 'schedule/result.html')