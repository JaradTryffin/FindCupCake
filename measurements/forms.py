from django import forms
from .models import Measurements

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = ['start_point','end_point','type_of_transport','price_per_km','price_per_hour']