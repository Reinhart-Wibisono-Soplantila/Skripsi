from django.urls import path
from .views import Dashboard
from . import views

app_name="app_dashboard"
urlpatterns = [
    path('', views.index, name='home'),
]