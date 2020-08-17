from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from gallery.forms import GalleryForm, PhotoCreateForm
from main.models import Gallery, Photo
from main.permissions import UserIsOwnerOrAdminMixin


class GalleryListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'gallery'
    template_name = 'gallery/gallery_list.html'
    paginate_by = 1

    def get_queryset(self):
        queryset = Gallery.objects.filter(user=self.request.user)
        return queryset


class GalleryCreateView(generic.CreateView):
    ''' создание галереи '''
    template_name = 'gallery/gallery_create.html'
    form_class = GalleryForm

    def post(self, request, *args, **kwargs):
        bindform = GalleryForm(request.POST)
        post = bindform.save(commit=False)
        post.user = request.user
        post.save()
        return HttpResponseRedirect('/gallery/list')


class GalleryDeleteView(generic.DeleteView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'gallery/gallery_delete.html'
    success_url = '/gallery/list'


class GalleryUpdateView(generic.UpdateView):
    template_name = 'gallery/gallery_update.html'
    form_class = GalleryForm
    context_object_name = 'gallery'
    success_url = '/gallery/list'

    def get_queryset(self):
        queryset = Gallery.objects.filter(pk=self.kwargs['pk'])
        return queryset


class PhotoGalleryList(generic.ListView):
    template_name = 'gallery/photo_list.html'
    context_object_name = 'photolist'
    paginate_by = 5

    def get_queryset(self):
        queryset = Photo.objects.filter(gallery=self.kwargs['pk'])
        return queryset


class PhotoDelete(generic.DeleteView):
    ''' Удаление фотки '''
    model = Photo
    template_name = 'gallery/photo_delete.html'
    success_url = '/gallery/list/'




class PhotoGalleryCreate(generic.CreateView):
    template_name = 'gallery/photo_create.html'

    def get_form(self, form_class=PhotoCreateForm):
        form = PhotoCreateForm(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        bindform = PhotoCreateForm(request.user, request.POST, files=request.FILES)
        # print('bindform.data=====>',bindform.data)
        gallery= bindform.data['gallery']
        if bindform.is_valid():
            post = bindform.save(commit=False)
            post.user = request.user
            post.save()
        # else:
        #     print('errors======>',bindform.errors)
        return HttpResponseRedirect('/gallery/photolist/{}'.format(gallery))
