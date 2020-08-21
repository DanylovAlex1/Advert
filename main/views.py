from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from main.permissions import UserIsOwnerOrAdminMixin
from .models import Advert, Photo, Gallery
from .forms import AdvertForm


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


class AdvertDetailView(LoginRequiredMixin, generic.DetailView):
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


class AdvertCreate(LoginRequiredMixin, generic.CreateView):
    ''' создание нового объявления '''
    form_class = AdvertForm
    template_name = 'main/advertcreate.html'



class AdvertUpdate(UserIsOwnerOrAdminMixin, generic.UpdateView):
    ''' Редактирование объявления '''
    permission_required = 'firstproject.nge_advert'

    model = Advert
    form_class = AdvertForm
    template_name = 'main/advertupdate.html'
    context_object_name = 'adv'


class AdvertDelete(UserIsOwnerOrAdminMixin, generic.DeleteView):
    ''' Удаление объявления '''
    model = Advert
    context_object_name = 'adv'
    template_name = 'main/advert_confirm_delete.html'
    success_url = '/'


class GalleryListView(generic.ListView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'main/gallery_create.html'


class GalleryCreateView(generic.CreateView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'main/gallery_create.html'


class GalleryUpdateView(generic.UpdateView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'main/gallery_create.html'

class GalleryDeleteView(generic.DeleteView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'main/gallery_create.html'
