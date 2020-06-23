from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


class News(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название Новости')
    date = models.DateTimeField(auto_now_add=True)
    post = models.TextField(verbose_name='Текст')
    isHidden = models.BooleanField(default=False)

    def __str__(self):
        return '%s / %s' % (self.title, self.date)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Promo(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок Объявления')
    dateSTART = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время начала показа')
    # dateEND = models.DateTimeField(blank=True, verbose_name='Дата и время окончания показа', default=timezone.now + 10) # NOTE подумать
    post = models.TextField(verbose_name='Текст')
    isHidden = models.BooleanField(default=False)
    img = models.ImageField(verbose_name='Превью 600x600', blank=True, width_field=601, height_field=601)

    def __str__(self):
        return '%s / %s' % (self.title, self.dateSTART)

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Реклама'
