from django.shortcuts import render

# Create your views here.
def outlets_index(request):
    return render(request, 'tables/outlets/index.html')

def outlets_create(request):
    return render(request, 'tables/outlets/create.html')

def outlets_update(request):
    return render(request, 'tables/outlets/update.html')

def outlets_view(request):
    return render(request, 'tables/outlets/view.html')


def vehicles_index(request):
    return render(request, 'tables/vehicles/index.html')

def vehicles_create(request):
    return render(request, 'tables/vehicles/create.html')

def vehicles_update(request):
    return render(request, 'tables/vehicles/update.html')

def vehicles_view(request):
    return render(request, 'tables/vehicles/view.html')