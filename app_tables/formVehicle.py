from django import forms
from .models import VehicleModel

class VehicleForm(forms.ModelForm):
    class Meta:
        model=VehicleModel
        fields=[
            'FullName',
            'VehicleNumber'
        ]
        
        labels = {
            'FullName' : 'Nama Lengkap',
            'VehicleNumber' : 'Nomor Kendaraan'
        }
        
        widgets = {
            'FullName': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Nama Driver"
                }
            ),
            'VehicleNumber' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Nomor Plat Kendaraan"
                }
            ),
        }