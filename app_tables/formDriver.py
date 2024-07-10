from django import forms
from .models import DriverModel

class DriverForm(forms.ModelForm):
    class Meta:
        model=DriverModel
        fields=[
            'FullName',
            'Phone',
            'Email',
            'Address',
        ]
        
        labels = {
            'FullName' : 'Nama Lengkap',
            'Phone' : 'Nomor Telepon',
            'Email' : 'Email',
            'Address' : 'Alamat'
        }
        
        widgets = {
            'FullName': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Nama Lengkap"
                }
            ),
            'Phone' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Nomor Telepon"
                }
            ),
            'Email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Alamat Email"
                }
            ),
            'Address' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Alamat Rumah"
                }
            ),
        }