from django.shortcuts import render

# Create your views here.
def outlets_index(request):
    return render(request, 'tables/outlets_index.html')

def vehicles_index(request):
    return render(request, 'tables/vehicles_index.html')