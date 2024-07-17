from django import forms
from .models import DriverModel, VehicleModel, OutletModel
from .models import reg_Provinces, reg_Regencies, reg_Districts, reg_Villages

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
    
    Provinsi = forms.ModelChoiceField(
        queryset=reg_Provinces.objects.all(), 
        empty_label='Pilih Provinsi',
        # required=True,
        widget=forms.Select(
            attrs={
                'class' : 'form-select form-control'
            }
        )
    )
    Kabupaten = forms.ModelChoiceField(
        queryset=reg_Regencies.objects.none(), 
        empty_label='Pilih Kabupaten',
        # required=False,
        widget=forms.Select(
            attrs={
                'class' :'form-select form-control'
            }
        )
    )
    Kecamatan = forms.ModelChoiceField(
        queryset=reg_Districts.objects.none(), 
        empty_label='Pilih Kecamatan',
        # required=False,
        widget=forms.Select(
            attrs={
                'class' :'form-select form-control'
            }
        )
    )
    Kelurahan = forms.ModelChoiceField(
        queryset=reg_Villages.objects.none(),
        empty_label='Pilih Kelurahan',
        # required=False,
        widget=forms.Select(
            attrs={
                'class' :'form-select form-control'
            }
        )
    )
    
    # def __init__(self, instance, *args, **kwargs):
    #     instance = kwargs.pop('instance', None)
    #     super().__init__(*args, **kwargs)
        
    #     # Set initial queryset for regency, district, and village to none
    #     self.fields['Kabupaten'].queryset = reg_Regencies.objects.none()
    #     self.fields['Kecamatan'].queryset = reg_Districts.objects.none()
    #     self.fields['Kelurahan'].queryset = reg_Villages.objects.none()
        
        # if instance and instance.Provinsi:
        #     # Set initial values for the form fields based on the instance
        #     self.fields['Provinsi'].initial = instance.Provinsi
        #     self.fields['Kabupaten'].queryset = reg_Regencies.objects.filter(province=instance.Provinsi).order_by('name')
        
        # if instance and instance.Kabupaten:
        #     self.fields['Kabupaten'].initial = instance.Kabupaten
        #     self.fields['Kecamatan'].queryset = reg_Districts.objects.filter(regency=instance.Kabupaten).order_by('name')
        
        # if instance and instance.Kecamatan:
        #     self.fields['Kecamatan'].initial = instance.Kecamatan
        #     self.fields['Kelurahan'].queryset = reg_Villages.objects.filter(district=instance.Kecamatan).order_by('name')
        
        # if instance and instance.Kelurahan:
        #     self.fields['Kelurahan'].initial = instance.Kelurahan
        # else:
        #     if 'Provinsi' in self.data:
        #         try:
        #             province_id = int(self.data.get('Provinsi'))
        #             self.fields['Kabupaten'].queryset = reg_Regencies.objects.filter(province_id=province_id).order_by('name')
        #         except (ValueError, TypeError):
        #             pass  # Invalid input from form submission; ignore and fallback to empty queryset

        #     if 'Kabupaten' in self.data:
        #         try:
        #             regency_id = int(self.data.get('Kabupaten'))
        #             self.fields['Kecamatan'].queryset = reg_Districts.objects.filter(regency_id=regency_id).order_by('name')
        #         except (ValueError, TypeError):
        #             pass  # Invalid input from form submission; ignore and fallback to empty queryset

        #     if 'Kecamatan' in self.data:
        #         try:
        #             district_id = int(self.data.get('Kecamatan'))
        #             self.fields['Kelurahan'].queryset = reg_Villages.objects.filter(district_id=district_id).order_by('name')
        #         except (ValueError, TypeError):
        #             pass  # Invalid input from form submission; ignore and fallback to empty queryset
            
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Kabupaten'].queryset = reg_Regencies.objects.none()
        self.fields['Kecamatan'].queryset = reg_Districts.objects.none()
        self.fields['Kelurahan'].queryset = reg_Villages.objects.none()

        if 'Provinsi' in self.data:
            try:
                province_id = int(self.data.get('Provinsi'))
                self.fields['Kabupaten'].queryset = reg_Regencies.objects.filter(province_id=province_id).order_by('name')
            except (ValueError, TypeError):
                pass  # Invalid input from form submission; ignore and fallback to empty queryset

        if 'Kabupaten' in self.data:
            try:
                regency_id = int(self.data.get('Kabupaten'))
                self.fields['Kecamatan'].queryset = reg_Districts.objects.filter(regency_id=regency_id).order_by('name')
            except (ValueError, TypeError):
                pass  # Invalid input from form submission; ignore and fallback to empty queryset

        if 'Kecamatan' in self.data:
            try:
                district_id = int(self.data.get('Kecamatan'))
                self.fields['Kelurahan'].queryset = reg_Villages.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # Invalid input from form submission; ignore and fallback to empty queryset

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
            'Address',
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
            'Address' : 'Alamat',
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
            'Address' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Alamat 2"
                }
            ),
            # 'Provinsi' : forms.TextInput(
            #     attrs = {
            #         'class' : 'form-control',
            #         'placeholder' : "Masukkan Provinsi"
            #     }
            # ),
            # 'Kabupaten' : forms.TextInput(
            #     attrs = {
            #         'class' : 'form-control',
            #         'placeholder' : "Masukkan Kabupaten"
            #     }
            # ),
            # 'Kecamatan' : forms.TextInput(
            #     attrs = {
            #         'class' : 'form-control',
            #         'placeholder' : "Masukkan Kecamatan"
            #     }
            # ),
            # 'Kelurahan' : forms.TextInput(
            #     attrs = {
            #         'class' : 'form-control',
            #         'placeholder' : "Masukkan Kelurahan"
            #     }
            # ),
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

class OutletViewForm(forms.ModelForm):
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
            'Address',
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
            'Address' : 'Alamat',
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
            'Address' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : "Masukkan Alamat 2"
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