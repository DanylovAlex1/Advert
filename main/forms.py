from django import forms
from django.utils.datastructures import MultiValueDict

from main.models import Advert, Photo, Gallery


class AdvertForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            pk = user
        else:
            pk = self.instance.user

        self.fields['gallery'].queryset = Gallery.objects.filter(user=pk)

    class Meta:
        model = Advert
        fields = ['title', 'text', 'phone', 'email', 'gallery']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gallery': forms.Select(attrs={'class': 'form-control'}),
        }


#
#
# class AdvertUpdateForm(forms.ModelForm):
#     def __init__(self, pk=None,
#                  title=None,
#                  user=None,
#                  text=None,
#                  phone=None,
#                  email=None, *args, **kwargs):
#         super(AdvertForm, self).__init__(*args, **kwargs)
#
#         self.fields['title'].initial = title
#         self.fields['text'].initial = text
#         self.fields['phone'].initial = phone
#         self.fields['email'].initial = email
#         self.fields['gallery'].queryset = Gallery.objects.filter(user=user)
#
#     class Meta:
#         model = Advert
#         fields = ['title', 'text', 'phone', 'email', 'gallery']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'text': forms.Textarea(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'gallery': forms.Select(attrs={'class': 'form-control'}),
#         }
#


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
