from django import forms
from app_outlet.models import OutletModel

class ScheduleForm(forms.Form):
    datas=forms.ModelMultipleChoiceField(
        queryset=OutletModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )