from django import forms
from .models import Icyangombwa


class Kwiyandikisha(forms.ModelForm):
    class Meta:
        model = Icyangombwa
        fields = '__all__'
