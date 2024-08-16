from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'password1' : forms.PasswordInput(
                attrs = {
                    'class' : 'form-control',
                }
            ),
            'password2' : forms.PasswordInput(
                attrs = {
                    'class' : 'form-control',
                }
            ),
        }
        
class LoginForm(AuthenticationForm):
    username=forms.CharField(
        label='Username', widget=forms.TextInput(
            attrs={
                'placeholder' : 'Username'
            }
        )
    )
    password=forms.CharField(
        label='Password', widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Password'
            }
        )
    )