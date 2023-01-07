from django import forms


class MassForm(forms.Form):
    date = forms.DateField(label='Igihe cya Missa',  widget=forms.DateInput(format="%d/%m/%Y",
                                                                            attrs={'class': 'form-control', 'type': 'date', 'min': 'date.now'}))
    time = forms.TimeField(label='Igihe cya Missa', widget=forms.TimeInput(
        attrs={'class': 'form-control', 'type': 'time'}))
    padiri = forms.CharField(label='Padri urasoma  Missa', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' Padri urasoma  Missa'}))
    place = forms.CharField(label='Padri Aho missa irabera', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' Aho Missa irabera'}))
    verse_1 = forms.CharField(label='Aho dusanga isomo rya mbere ', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' Aho dusanga isomo rya mbere'}))
    isomo_1 = forms.CharField(label='Isomo rya mbere ', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': ' Isomo rya mbere'}))
    verse_2 = forms.CharField(label='Aho dusanga isomo rya Kabiri ', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' Aho dusanga isomo rya Kabiri'}))
    isomo_2 = forms.CharField(label='Isomo rya Kabiri ', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': ' Isomo rya Kabiri'}))
    ivanjiri_verse = forms.CharField(label='Aho dusanga ivanjiri ', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' Aho dusanga ivanjiri'}))
    ivanjiri = forms.CharField(label='Ivanjiri ', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': ' Ivanjiri'}))
    summary = forms.CharField(label='Hommerie', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': ' Hommerie'}))
    umwanzuro = forms.CharField(label='Umwanzuro wa Missa ', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': ' Umwanzuro wa Missa'}))
