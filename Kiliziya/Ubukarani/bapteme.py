from django import forms
from .models import Icyangombwa, Ibyasabwe


class Ibisabwa(forms.ModelForm):
    class Meta:
        Model = Ibyasabwe
        fields = '__all__'
        widgets = {
            'amazina': forms.TextInput(attrs={'type': 'readonly'}),
            'umubyeyi': forms.FileField(label='Icyangomwa cyumubyeyi wa Batisimu'),
            'umuryangoremezo': forms.FileField(label='Icyangomwa cyumuryango Remezo')

        }
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
    prenom = forms.CharField(label='Izina rya Gikristu', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Izina rya Gikristu'}))
    Nom = forms.CharField(label='Izina ryababyeyi', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'izina ryababyeyi'}))
    papa = forms.CharField(label='Amazina ya Papa', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Amazina ya papa'}))
    mama = forms.CharField(label='Amazina ya mama', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Amazina ya mama'}))
    umubyeyi_wa_batisimu = forms.CharField(label='Umubyeyi wa Batisimu', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Umubyeyi wa Batisimu'}))
    parroise = forms.CharField(label='Parroise', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Parroise'}))
    Vicus = forms.CharField(label='Domicillium', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Domicillium;vicus'}))
    province = forms.CharField(label='Intara', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Intara'}))
    District = forms.CharField(label='Akarere', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Akarere'}))
    itariki_yamavuko = forms.DateTimeField(
        label='itariki ya mavuko', widget=forms.DateTimeInput(attrs={'class': 'form-group', 'type': 'date', 'min': '1900-01-01'}))
    batisimu = forms.DateTimeField(
        label='itariki ya Batisimu', widget=forms.DateTimeInput(attrs={'class': 'form-group', 'type': 'date'}))
    Ukaristiya = forms.DateTimeField(
        label='igihe yaherewe Ukaristiya', widget=forms.DateTimeInput(attrs={'class': 'form-group', 'type': 'date'}))
    Gukomezwa = forms.DateTimeField(
        label='igihe yaherewe Ukaristiya', widget=forms.DateTimeInput(attrs={'class': 'form-group', 'type': 'date'}))

    batisimu_status = forms.BooleanField(required=False)
    Ukaristiya_status = forms.BooleanField(required=False)
    Gukomezwa_status = forms.BooleanField(required=False)

    def clean_amazina(self):
        return self.cleaned_data['amazina'].capitalize()
    # amazina = forms.CharField(label='Amazina', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Amazina'})),
    # amazina = forms.CharField(label='Amazina', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Amazina'})),
