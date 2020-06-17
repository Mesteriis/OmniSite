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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    firmID = models.OneToOneField(Firm, on_delete=models.CASCADE)
    # module = models // FIXME подумать
    isDialer = models.BooleanField(default=False)
    isAllowSubDealer = models.BooleanField(default=False)
    isFinanceBlock = models.BooleanField(default=False)
    comments = models.TextField(max_length=500, blank=True)
    personalSettingsSite = models.TextField(default=defaultSettings)
    avatar = models.ImageField(
        upload_to='userprofile/avatar/',
        blank=True,
        null=True,
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
