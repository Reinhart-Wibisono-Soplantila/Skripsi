"""proweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # path('', redirect('home/')),
    path('schedule/', include('app_schedules.urls', namespace='app_schedules')),
    path('vehicle/', include('app_vehicle.urls', namespace='app_vehicle')),
    path('outlet/', include('app_outlet.urls', namespace='app_outlet')),
    path('home/', include('app_dashboard.urls')),
    path('report/', include('app_report.urls')),
    path('admin/', admin.site.urls),
]
