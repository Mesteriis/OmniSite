# Generated by Django 3.0.7 on 2020-06-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20200622_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='isSupportChat',
            field=models.BooleanField(default=False, verbose_name='Специалист ТП, доступ в чат'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='userprofile/avatar/email/'),
        ),
    ]