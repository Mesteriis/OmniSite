from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Firm(models.Model):
    pass


defaultSettings = {
    'colorThem': 'white',

}


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    # firmID = models.OneToOneField(Firm, on_delete=models.CASCADE,  blank=True)
    # module = models // FIXME подумать
    isDialer = models.BooleanField(default=False, blank=True)
    isAllowSubDealer = models.BooleanField(default=False)
    isFinanceBlock = models.BooleanField(default=False)
    comments = models.TextField(max_length=500, blank=True)
    personalSettingsSite = models.TextField(default=defaultSettings)
    avatar = models.ImageField(
        upload_to='userprofile/avatar/' + str(User.EMAIL_FIELD) + '/',
        blank=True,
        null=True,
    )
    wialonToken = models.TextField(max_length=100, blank=True)
    omnikomToken = models.TextField(max_length=100, blank=True)
    isSupportChat = models.BooleanField(default=False, verbose_name="Специалист ТП, доступ в чат")

    def __str__(self):
        return '%s из %s' % (self.user, self.location)

    class Meta:
        verbose_name = 'Профиль для пользователя'
        verbose_name_plural = 'Профили пользователей'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Notification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True, verbose_name='Дaта и время получения')
    isMarkRead = models.BooleanField(default=False)
    title = models.TextField(max_length=120, blank=False, default='Заголовок уведомления')
    text = models.TextField(max_length=500, blank=False, default='Текст уведомления')
    link = models.URLField(blank=True, default='localhost:8000:/dashboard')

    def __str__(self):
        return '%s / %s' % (self.user, self.title)

    class Meta:
        verbose_name = 'Уведомление для пользователя'
        verbose_name_plural = 'Уведомления для пользователя'
