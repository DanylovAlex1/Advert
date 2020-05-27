from django.contrib import admin
from .models import Advert  # Нужно импортировать можель, чтоб она была тут доступна


admin.site.register(Advert)
