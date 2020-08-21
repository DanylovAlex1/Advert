from django.contrib import admin
from .models import Advert, Photo, Gallery


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    search_fields = ['title', 'text', 'email']
    list_filter = ('user',)


@admin.register(Photo)
class PhototAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('gallery',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('user',)
