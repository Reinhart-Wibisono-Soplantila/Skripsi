from django import forms
from .models import DriverModel, VehicleModel

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
            'Address' : 'Alamat',
        }
        
        error_messages ={
            'FullName' : {
                'max_length' : 'Nama terlalu panjang'
            },
            'Email' : {
                'max_length': '*Email terlalu panjang',
                'unique': "*Email sudah digunakan",
            },'Phone' : {
                'max_length' : '*Nomor Telepon terlalu panjang'
            },'Address' : {
                'max_length' : '*Alamat terlalu panjang'
            },
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


class VehicleForm(forms.ModelForm):
    StatusChoices=(
        ("Ready", 'Ready'),
        ('Repaired', 'Repaired'),
        ('Used', 'Used'),
    )
    Status = forms.ChoiceField(
        choices=StatusChoices,
        required=False,
        widget=forms.Select(
            attrs={
                'class' :'form-select form-control'
            }
        )
    )
    class Meta:
        model=VehicleModel
        fields = [
            'UnitType',
            'VehicleNumber',
            'Status',
        ]
        
        labels = {
            'UnitType' : 'Tipe Kendaraan',
            'VehicleNumber' : 'Nomor Kendaraan'
        }
        
        error_messages ={
            'UnitType' : {
                'max_length' : 'Tipe Kendaraan terlalu panjang'
            },
            'VehicleNumber' : {
                'max_length': 'Nomor Kendaraan terlalu panjang',
                'unique': "Nomor Kendaraan sudah digunakan",
            }
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
        