from django import forms

from main.models import Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }



