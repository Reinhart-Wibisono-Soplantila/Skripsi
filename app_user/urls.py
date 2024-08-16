from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name='app_user'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='app_user:login'), name='logout'),
]