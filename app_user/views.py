from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .form import RegisterForm, LoginForm, ProfileForm, MyPasswordChangeForm

def index(request):
    userObject = User.objects.all()
    context={
        'UserObject' : userObject
    }
    return render(request, 'user/index.html', context)

def profile(request):
    profileForm = ProfileForm(instance=request.user)
    passwordForm = MyPasswordChangeForm(user=request.user)
    if request.method == 'POST':
        if 'updateProfile' in request.POST:
            profileForm = ProfileForm(request.POST, instance=request.user)
            if profileForm.is_valid():
                profileForm.save()
                messages.success(request, 'Your profile was successfully updated!')
                return redirect('app_user:profile')
        elif 'changePassword' in request.POST:
            passwordForm = MyPasswordChangeForm(user=request.user, data=request.POST)
            if passwordForm.is_valid():
                user = passwordForm.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('app_user:profile')
            else:
                print(passwordForm.errors)
    context={
        'profileForm':profileForm,
        'passwordForm':passwordForm
    }
    return render(request, 'user/profile.html', context)

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context={
            'form' : form,
        }
        return render(request, 'user/register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST or None)
        error={}
        print(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            print('success')
            return redirect('app_dashboard:home')
        else:
            print('failed')
            error=form.errors
        context={
            'form':form,
            'error':error
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
            messages.error(request, "Invalid Input.")
        return render(request, 'user/login.html', context)