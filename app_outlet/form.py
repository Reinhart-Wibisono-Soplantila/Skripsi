from django import forms
from .models import OutletModel

class OutletForm(forms.ModelForm):
    
    # Provinsi = forms.ModelChoiceField(
    #     queryset=reg_Provinces.objects.all(), 
    #     empty_label='Pilih Provinsi',
    #     # required=True,
    #     widget=forms.Select(
    #         attrs={
    #             'class' : 'form-select form-control'
    #         }
    #     )
    # )
    # Kabupaten = forms.ModelChoiceField(
    #     queryset=reg_Regencies.objects.none(), 
    #     empty_label='Pilih Kabupaten',
    #     # required=False,
    #     widget=forms.Select(
    #         attrs={
    #             'class' :'form-select form-control'
    #         }
    #     )
    # )
    # Kecamatan = forms.ModelChoiceField(
    #     queryset=reg_Districts.objects.none(), 
    #     empty_label='Pilih Kecamatan',
    #     # required=False,
    #     widget=forms.Select(
    #         attrs={
    #             'class' :'form-select form-control'
    #         }
    #     )
    # )
    # Kelurahan = forms.ModelChoiceField(
    #     queryset=reg_Villages.objects.none(),
    #     empty_label='Pilih Kelurahan',
    #     # required=False,
    #     widget=forms.Select(
    #         attrs={
    #             'class' :'form-select form-control'
    #         }
    #     )
    # )
            
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['Kabupaten'].queryset = reg_Regencies.objects.none()
    #     self.fields['Kecamatan'].queryset = reg_Districts.objects.none()
    #     self.fields['Kelurahan'].queryset = reg_Villages.objects.none()

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