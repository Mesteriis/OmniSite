# Generated by Django 3.0.7 on 2020-06-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='omnikomToken',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='wialonToken',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]