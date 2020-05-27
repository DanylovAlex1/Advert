from django.shortcuts import render
from django.views import generic
from .models import Advert
from .forms import AdvertForm


class AdvertListView(generic.ListView):
    ''' Список рекламных объявлeний '''
    queryset = Advert.objects.all()
    template_name = 'main/advertlist.html'
    context_object_name = 'adv'


class AdvertDetailView(generic.DetailView):
    '''детализированная форма объявления'''
    # queryset =Advert.obgects.get()
    model = Advert
    template_name = 'main/advertdetail.html'
    context_object_name = 'adv'


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

