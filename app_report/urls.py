from django.urls import path
from . import views

app_name='app_report'
urlpatterns = [
    path('', views.index, name='index'),
    path('view/<str:Schedule_id>', views.view, name='view'),
    path('maps/<str:Schedule_id>/<str:vehicle_number>/', views.maps, name='maps'),
    path('delete/<str:Schedule_id>', views.delete, name='delete')
]
