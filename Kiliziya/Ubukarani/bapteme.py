from django import forms
from .models import Icyangombwa


# class Kwiyandikisha(forms.ModelForm):
#     class Meta:
#         model = Icyangombwa
#         fields = '__all__'
#         widgets = {
#             'amazina': forms.TextInput(attrs={'label': 'Amazina', 'class': 'form-control', 'placeholder': 'Amazina'}),
#             'papa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amazina ya Papa'}),
#             'mama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amazina ya Mama'}),
#             'umubyeyi_wa_batisimu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Umubyeyi wa batisimu'}),
#             'parroise': forms.TextInput(attrs={'class': 'form-control'}),
#             'itariki_yamavuko': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'itariki/ukwezi/umwaka'}),
#             'batisimu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'itariki/ukwezi/umwaka'}),
#             'Ukaristiya': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'itariki/ukwezi/umwaka'}),
#             'Gukomezwa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'itariki/ukwezi/umwaka'}),
#             'batisimu_status': forms.BooleanField(),
#             'Ukaristiya_status': forms.TextInput(attrs={'class': 'form-control'}),
#             'Gukomezwa_status': forms.TextInput(attrs={'class': 'form-control'})

# }


class RawKwiyandikisha(forms.Form):
    amazina = forms.CharField(label='Amazina', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Amazina'}))
    papa = forms.CharField(label='Amazina ya Papa', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Amazina ya papa'}))
    mama = forms.CharField(label='Amazina ya mama', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Amazina ya mama'}))
    umubyeyi_wa_batisimu = forms.CharField(label='Umubyeyi wa Batisimu', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Umubyeyi wa Batisimu'}))
    parroise = forms.CharField(label='Parroise', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Parroise'}))
    itariki_yamavuko = forms.DateField(
        label='itariki ya mavuko', widget=forms.SelectDateWidget(attrs={'class': 'form-group', 'type': 'date', 'min': '1900-01-01'}))
    batisimu = forms.DateField(
        label='itariki ya Batisimu', widget=forms.SelectDateWidget(attrs={'class': 'form-group', 'type': 'date'}))
    Ukaristiya = forms.DateField(
        label='igihe yaherewe Ukaristiya', widget=forms.SelectDateWidget(attrs={'class': 'form-group', 'type': 'date'}))
    Gukomezwa = forms.DateField(
        label='igihe yaherewe Ukaristiya', widget=forms.SelectDateWidget(attrs={'class': 'form-group', 'type': 'date'}))

    batisimu_status = forms.BooleanField(required=False)
    Ukaristiya_status = forms.BooleanField(required=False)
    Gukomezwa_status = forms.BooleanField(required=False)
    # amazina = forms.CharField(label='Amazina', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Amazina'})),
    # amazina = forms.CharField(label='Amazina', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Amazina'})),
