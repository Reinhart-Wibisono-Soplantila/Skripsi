from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group, Permission

class ProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'email']
        widgets={
            'username':forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control'
                }
            )
        } 
        labels={
            'username':'Username',
            'email' : 'Email'
        }
        help_texts = {
            'username': '',
        }
    # def clean_username(self):
    #     new_username = self.cleaned_data.get('username')
    #     if new_username == self.instance.username:
    #         raise forms.ValidationError("Username cannot be same.")
    #     return new_username

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control', 
                }))
    password2=forms.CharField(
        label='Confirmation Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control', 
                }))
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                }
            )
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email
             
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
    
class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(MyPasswordChangeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label