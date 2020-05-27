from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='adminka'),
    path('', include('main.urls')),  # подключаем файл urls.py из приложения main

]
