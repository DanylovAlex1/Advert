from django.shortcuts import render
from django.views import generic
#from django.core.paginator import Paginator
from .models import Advert, Photo
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




class AdvertDetailView(generic.DetailView):
    '''детализированная форма объявления'''
    # queryset =Advert.obgects.get()
    model = Advert
    template_name = 'main/advertdetail.html'
    context_object_name = 'adv'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo'] = Photo.objects.filter(advert=self.kwargs['pk'])
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
