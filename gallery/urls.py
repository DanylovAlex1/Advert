from django.urls import path

from gallery.views import GalleryListView, GalleryCreateView, GalleryUpdateView, GalleryDeleteView, PhotoGalleryList

urlpatterns=[
    path('list/',GalleryListView.as_view(), name='gallery_list'),
    path('create/', GalleryCreateView.as_view(), name='gallery_create'),
    path('update/<int:pk>', GalleryUpdateView.as_view(), name='gallery_update'),
    path('delete/<int:pk>', GalleryDeleteView.as_view(), name='gallery_delete'),

    path('photolist/<int:pk>', PhotoGalleryList.as_view(), name='photo_gallery_list'),


]
