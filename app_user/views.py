from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .form import RegisterForm, LoginForm
from django.views import View

# Create your views here.
def index(request):
    context={
        'Head' : 'INDEX USER'
    }
    print(request.user)
    return render(request, 'user/index.html', context)

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context={
            'form' : form,
        }
        return render(request, 'user/register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('app_dashboard:home')
        context={
            'form':form
        }
        return render(request, 'user/register.html', context)
    
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form':form
        }
        return render(request, 'user/login.html', context)
    
    def post(self, request):
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app_dashboard:home')
        context = {
            'form':form
        }
        return render(request, 'user/login.html', context)