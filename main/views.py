from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import generic
from main.permissions import UserIsOwnerOrAdminMixin
from .models import Advert, Photo
from .forms import AdvertForm


class AdvertListView(generic.ListView):
    ''' Список рекламных объявлeний '''
    #    queryset = Advert.objects.all()
    template_name = 'main/advertlist.html'
    context_object_name = 'adv'
    paginate_by = 2

    def get_queryset(self):
        if self.request.GET.get('val'):
            value = self.request.GET.get('val')
            queryset = Advert.objects.filter(text__contains=value)
        else:
            queryset = Advert.objects.all()
        return queryset


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
        context['permit'] = UserIsOwnerOrAdminMixin.has_permission(self)
        return context


class AdvertCreate(LoginRequiredMixin, generic.CreateView):
    ''' создание нового объявления '''
    # form_class = AdvertForm
    template_name = 'main/advertcreate.html'

    def get_form(self, form_class=AdvertForm):
        form = AdvertForm(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        bindform = AdvertForm(request.user, request.POST)
        post = bindform.save(commit=False)
        post.user = request.user
        post.save()
        return HttpResponseRedirect('/')


class AdvertUpdate(UserIsOwnerOrAdminMixin, generic.UpdateView):
    ''' Редактирование объявления '''
    permission_required = 'firstproject.nge_advert'
    template_name = 'main/advertupdate.html'
    form_class = AdvertForm

    def get_queryset(self):
        queryset = Advert.objects.filter(pk=self.kwargs['pk'])
        return queryset

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.user = self.request.user
        return form


class AdvertDelete(UserIsOwnerOrAdminMixin, generic.DeleteView):
    ''' Удаление объявления '''
    model = Advert
    context_object_name = 'adv'
    template_name = 'main/advert_confirm_delete.html'
    success_url = '/'
