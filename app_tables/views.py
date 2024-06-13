from django.shortcuts import render

# Create your views here.
def outlets_index(request):
    return render(request, 'tables/outlets/index.html')

def outlets_create(request):
    return render(request, 'tables/outlets/create.html')



def vehicles_index(request):
    return render(request, 'tables/vehicles/index.html')