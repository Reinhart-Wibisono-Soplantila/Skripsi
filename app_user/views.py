from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .form import RegisterForm, LoginForm
from django.contrib import messages
from django.views import View

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
        context = {
            'form':form
        }
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print('okee')
                user = form.get_user()
                login(request, user)
                return redirect('app_dashboard:home')
            else:
                messages.error(request, "Wrong Username or Wrong Password.")
        else:
            messages.error(request, "Wrong Username or Wrong Password.")
        return render(request, 'user/login.html', context)