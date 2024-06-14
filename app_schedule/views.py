from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'schedule/index.html')

def overview(request):
    return render(request, 'schedule/overview.html')

def vehicle(request):
    return render(request, 'schedule/vehicle.html')

def result(request):
    return render(request, 'schedule/result.html')