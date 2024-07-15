from django import forms
from .models import DriverModel, VehicleModel, OutletModel

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
                'max_length' : 'FullName terlalu panjang'
            },
            'Email' : {
                'max_length': 'Email terlalu panjang',
                'unique': "Email sudah digunakan",
            },'Phone' : {
                'max_length' : 'Phone terlalu panjang'
            },'Address' : {
                'max_length' : 'Address terlalu panjang'
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

class OutletForm(forms.ModelForm):
    DeliveryStatus=(
        ("Daily", 'Daily'),
        ('Weekly', 'Weekly')
    )
    
    Days=(
        ("Monday", 'Senin'),
        ("Tuesday", 'Selasa'),
        ('Wednesday', 'Rabu'),
        ("Thursday", 'Kamis'),
        ('Friday', 'Jumat'),
        ('Saturday', 'Sabtu')
    )
    
    Delivery = forms.ChoiceField(
        choices=DeliveryStatus,
        required=False,
        label='Jenis Pengiriman',
        widget=forms.Select(
            attrs={
                'class' :'form-select form-control'
            }
        )
    )
    
    Days = forms.ChoiceField(
        choices=Days,
        required=False,
        label='Hari Pengiriman',
        widget=forms.Select(
            attrs={
                'class' :'form-select form-control'
            }
        )
    )
    
    class Meta:
        model=OutletModel
        fields = [
            'OutletNumber',
            'OutletCode',
            'OutletName',
            'OutletType',
            'Address1',
            'Address2',
            'Town',
            'Provinsi',
            'Kabupaten',
            'Kecamatan',
            'Kelurahan',
            'Latitude',
            'Longitude',
            'Days',
            'Delivery',
        ]
        
        labels = {
            'OutletNumber' : 'Nomor Toko',
            'OutletCode' : 'Kode Toko',
            'OutletName' : 'Nama Toko',
            'OutletType' : 'Tipe Toko',
            'Address1' : 'Alamat 1',
            'Address2' : 'Alamat 2',
            'Town' : 'Kota',
            'Provinsi' : 'Provnsi',
            'Kabupaten' : 'Kabupaten',
            'Kecamatan' : 'Kecamatan',
            'Kelurahan' : 'Kelurahan',
            'Latitude' : 'Koordinat Latitude',
            'Longitude' : 'Koodinat Longitude',
        }
        
        widgets = {
            'OutletNumber' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Nomor Toko"
                }
            ),
            'OutletCode' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Kode Toko"
                }
            ),
            'OutletName' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Nama Toko"
                }
            ),
            'OutletType' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Tipe Toko"
                }
            ),
            'Address1' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Alamat 1"
                }
            ),
            'Address2' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Alamat 2"
                }
            ),
            'Town' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Kota"
                }
            ),
            'Provinsi' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Provinsi"
                }
            ),
            'Kabupaten' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Kabupaten"
                }
            ),
            'Kecamatan' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Kecamatan"
                }
            ),
            'Kelurahan' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Kelurahan"
                }
            ),
            'Latitude' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Koordinat Latitude"
                }
            ),
            'Longitude' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Koordinat Longitude"
                }
            ),
        }
        
class VehicleForm(forms.ModelForm):
    StatusChoices=(
        ("Ready", 'Ready'),
        ('Repaired', 'Repaired'),
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