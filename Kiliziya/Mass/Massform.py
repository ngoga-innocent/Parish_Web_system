from django import forms


class MassForm(forms.Form):
    time = forms.CharField(label='Igihe cya Missa', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Igihe cya Missa'}))
    padiri = forms.CharField(label='Padri urasoma  Missa', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' Padri urasoma  Missa'}))
    place = forms.CharField(label='Padri urasoma  Missa', widget=forms.TextInput(
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
