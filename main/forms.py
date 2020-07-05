from django import forms
from django.contrib.auth.models import User

from main.models import Advert, Photo


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = '__all__'
        #        fields = ['title', 'text', 'phone', 'email']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class PhotoCreateForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['user','title', 'image']

        # widgets = {
        #     'user': forms.ModelChoiceField(queryset=User.objects.all()),
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'image': forms.ImageField(attrs={'class': 'form-control'}),
        # }
        #

