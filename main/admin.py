from django.contrib import admin
from .models import Advert, Photo, Gallery

# подключаем к админке нашу модель  Advert
admin.site.register(Advert)
admin.site.register(Gallery)

#admin.site.register(Photo)
#
# @admin.register(Photo)
# class AdvertAdmin(admin.ModelAdmin):
#     search_fields = ['title']
#     list_filter = ('gallery',)
#

