from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name='adminka'),
    path('', include('main.urls')),  # подключаем файл urls.py из приложения main

    path('accounts/', include('allauth.urls')),
    path('gallery/', include('gallery.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)