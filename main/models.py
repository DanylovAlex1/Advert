from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.admin import User


def get_path_image(uname, iname):
    '''формирую имя файла картинки.
    к имени спереди добавляю путь - папку, с именем пользователя, где будет
    храниться картинка.
    Если этого не делать все будут в одной папке'''
    path = str(uname).lower() + '/' + str(iname)
    return path


class Gallery(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Описание', max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['title']

    def get_detailUrl(self):
        return reverse('gallery_update', kwargs={'pk': self.pk})

    def get_deleteUrl(self):
        return reverse('gallery_delete', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Advert(models.Model):
    '''
    Модель Advert, для хранения информации Рекламного объявления
    '''
    title = models.CharField(verbose_name='заглавие', max_length=50)
    text = models.TextField(verbose_name='Текст объявления', null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=20, null=True, blank=True)
    email = models.EmailField(verbose_name='Email', max_length=40, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_detailUrl(self):
        return reverse('adv_detail', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse("adv_list")

    def get_UpdateUrl(self):
        return reverse('adv_update', kwargs={'pk': self.pk})

    def get_DeleteUrl(self):
        return reverse('adv_delete', kwargs={'pk': self.pk})

    def get_photo_gallery_list(self):
        return reverse('photo_gallery_list', kwargs={'pk': self.pk})


class Photo(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Описание', max_length=50, blank=True, null=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='gallery/')
    # advert = models.ForeignKey(Advert, verbose_name='Объявление', on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        ''' переопределяю метод save
        чтоб изменить значения image.name
        '''
        self.image.name = get_path_image(self.user, self.image.name)
        super().save(*args, **kwargs)

    # def get_photogallerylistUrl(self):
    #     return reverse('photo_list', kwargs={'gallery': self.gallery})

    def get_PhotodeleteUrl(self):
        return reverse('photo_delete', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотограция'
        verbose_name_plural = 'Фотографии'
        ordering = ['user', 'gallery', 'title']
