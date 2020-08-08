from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from gallery.forms import GalleryForm
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

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        # qsetGallery = Gallery.objects.filter(pk=self.kwargs['pk'])
        # gallery_id = qsetGallery.get().get('id')
        context = super().get_context_data(**kwargs)
        context['photo'] = Photo.objects.filter(gallery=pk)
        context['permit'] = UserIsOwnerOrAdminMixin.has_permission(self)
        return context





class PhotoGalleryCreate(generic.CreateView):
    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        # qsetGallery = Gallery.objects.filter(pk=self.kwargs['pk'])
        # gallery_id = qsetGallery.get().get('id')

        context = super().get_context_data(**kwargs)
        context['photo'] = Photo.objects.filter(gallery=pk)
        context['permit'] = UserIsOwnerOrAdminMixin.has_permission(self)
        return context
