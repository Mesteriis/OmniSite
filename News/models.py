from django.db import models

class News(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название Новости')
    date = models.DateTimeField(auto_now_add=True)
    post = models.TextField(verbose_name='Текст')
    isHidden = models.BooleanField(default=False)


    def __str__(self):
        return '%s / %s' % (self.title , self.date)


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'