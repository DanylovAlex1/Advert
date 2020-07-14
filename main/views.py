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


"""
https://docs.djangoproject.com/en/3.0/topics/auth/default/

The PermissionRequiredMixin mixin¶
To apply permission checks to class-based views, you can use the PermissionRequiredMixin:

class PermissionRequiredMixin¶
This mixin, just like the permission_required decorator, checks whether the user accessing a view has all given permissions. You should specify the permission (or an iterable of permissions) using the permission_required parameter:

from django.contrib.auth.mixins import PermissionRequiredMixin

class MyView(PermissionRequiredMixin, View):
    permission_required = 'polls.add_choice'
    # Or multiple of permissions:
    permission_required = ('polls.view_choice', 'polls.change_choice')
You can set any of the parameters of AccessMixin to customize the handling of unauthorized users.

You may also override these methods:

get_permission_required()¶
Returns an iterable of permission names used by the mixin. Defaults to the permission_required attribute, converted to a tuple if necessary.

has_permission()¶
Returns a boolean denoting whether the current user has permission to execute the decorated view. By default, this returns the result of calling has_perms() with the list of permissions returned by get_permission_required().
"""
