from django import forms

from main.models import Gallery, Photo


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }



class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['user', 'title', 'image']

        # widgets = {
        #     'user': forms.ModelChoiceField(queryset=User.objects.all()),
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'image': forms.ImageField(attrs={'class': 'form-control'}),
        # }
        #



