from django import forms
from .models import Cooperative

class CooperativeForm(forms.ModelForm):
    class Meta:
        model = Cooperative
        fields = '__all__'
        