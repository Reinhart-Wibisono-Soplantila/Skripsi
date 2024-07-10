from django import forms
from .models import VehicleModel

class VehicleForm(forms.ModelForm):
    class Meta:
        model=VehicleModel
        fields=[
            'UnitType',
            'VehicleNumber',
        ]
        
        labels = {
            'UnitType' : 'Tipe Kendaraan',
            'VehicleNumber' : 'Nomor Kendaraan'
        }
        
        widgets = {
            'UnitType': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Tipe Kendaraan"
                }
            ),
            'VehicleNumber' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Nomor Plat Kendaraan"
                }
            ),
        }