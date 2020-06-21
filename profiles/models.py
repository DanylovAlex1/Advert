from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    '''Расширение профиля пользователя'''
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    firstname = models.CharField(blank=True, null=True, max_length=30, verbose_name='Имя')
    lastname = models.CharField(blank=True, null=True, max_length=30, verbose_name='Фамилия')
    avatar = models.ImageField(verbose_name='Avatar',
                               default='profiles/avatar.png',
                               upload_to='profiles/', null=True, blank=True)
    phone = models.CharField(blank=True, null=True, max_length=30, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


    def get_absotute_url(self):
        return reverse('user_profile', kwargs={'pk': self.pk})

    ''' поскольку я расширил модель пользователя(моделью Profile),
    то мне нужно чтоб при создании ползователя 
    автоматически создавалось и его расширение.
    Я ловлю сохранение модели User : (post_save,sender=User)
    и заполняю модель Profile
    по сути я создаю пустую запись, 
    но со ссылкой OneToOneField на созданного пользователя
    '''

    @receiver(post_save, sender=User)# ловлю событие post_save для модели User
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, id=instance.id)

    @receiver
    def save_user_profile(sender, instance, **kwargs):
        instance.pofile.save()

