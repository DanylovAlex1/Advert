from django.urls import path

from gallery.views import GalleryListView, GalleryCreateView, GalleryUpdateView, GalleryDeleteView

urlpatterns=[
    path('list/',GalleryListView.as_view(), name='gallery_list'),
    path('create/', GalleryCreateView.as_view(), name='gallery_create'),
    path('update/<int:pk>', GalleryUpdateView.as_view(), name='gallery_update'),
    path('delete/<int:pk>', GalleryDeleteView.as_view(), name='gallery_delete'),


]
