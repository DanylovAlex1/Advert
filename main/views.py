from django.shortcuts import render
from django.views import generic
# from django.core.paginator import Paginator
from .models import Advert, Photo, Gallery
from .forms import AdvertForm, PhotoCreateForm


class AdvertListView(generic.ListView):
    ''' Список рекламных объявлeний '''
    queryset = Advert.objects.all()
    template_name = 'main/advertlist.html'
    # paginator=Paginator(queryset,2)
    # page_number= request.GET.get('page',1)
    # page= paginator.get_page(page_number)
    # queryset=page.object_list
    context_object_name = 'adv'
    paginate_by = 2


class AdvertDetailView(generic.DetailView):
    '''детализированная форма объявления'''
    model = Advert
    template_name = 'main/advertdetail.html'
    context_object_name = 'adv'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        qsetAdvert = Advert.objects.values('gallery_id').filter(pk=pk)
        gallery = qsetAdvert.get().get('gallery_id')

        context = super().get_context_data(**kwargs)
        context['photo'] = Photo.objects.filter(gallery=gallery)
        return context


class AdvertCreate(generic.CreateView):
    ''' создание нового объявления '''
    form_class = AdvertForm
    template_name = 'main/advertcreate.html'


class AdvertUpdate(generic.UpdateView):
    ''' Редактирование объявления '''
    model = Advert
    form_class = AdvertForm
    template_name = 'main/advertupdate.html'
    context_object_name = 'adv'


class AdvertDelete(generic.DeleteView):
    ''' Удаление объявления '''
    model = Advert
    context_object_name = 'adv'
    template_name = 'main/advert_confirm_delete.html'
    success_url = '/'


class GalleryCreateView(generic.CreateView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'main/gallery_create.html'

#
# class UsersAddPhotoView(generic.CreateView):
#
#     model = Photo
#     context_object_name = 'photo'
#     form_class=PhotoCreateForm
#     template_name = 'main/add_photo.html'
#     success_url = 'photos_list'
#
#
#
#
#
# class PhotolistView(generic.ListView):
#
#     def get_queryset(self):
#         user=self.request.user
#         return Photo.objects.filter(user=user)
#     template_name = 'main/user_photolist.html'
#     context_object_name = 'photolist'
