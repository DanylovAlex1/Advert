from django import forms
from main.models import Advert

class AdvertForm(forms.ModelForm):
    class Meta:
        model=Advert
        fields = '__all__'

#        fields = ['title', 'text', 'phone', 'email']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
