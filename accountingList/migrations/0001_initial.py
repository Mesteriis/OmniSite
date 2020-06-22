# Generated by Django 3.0.7 on 2020-06-22 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientFirm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='promisedPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='AccountingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата операции')),
                ('SaldoBefore', models.DecimalField(decimal_places=2, default='0.00', max_digits=8)),
                ('typeActivity', models.CharField(choices=[('dt', 'Приход'), ('ct', 'Расход'), ('pr', 'Обещанный платеж')], default='ct', max_length=2, verbose_name='Тип операции')),
                ('sum', models.PositiveIntegerField(verbose_name='Сумма операции')),
                ('SaldoAfter', models.DecimalField(decimal_places=2, default='0.00', max_digits=8)),
                ('Comment', models.CharField(max_length=300, verbose_name='Комментарий блокировки')),
                ('startDate', models.DateTimeField(default=None)),
                ('endDate', models.DateTimeField(default=None)),
                ('typeBlock', models.CharField(choices=[('fn', 'Финансовая блокировка'), ('tn', 'Техническая блокировка'), ('rs', 'Остальное')], default='fn', max_length=2, verbose_name='Тип блокировки')),
                ('isBlock', models.BooleanField(default=False, verbose_name='Заблокирован')),
                ('dateBlock', models.DateField(default='', verbose_name='Дата будущей блокировки')),
                ('BlockComment', models.CharField(max_length=300, verbose_name='Комментарий блокировки')),
                ('idClient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='accountingList.ClientFirm', verbose_name='Фирма клиента')),
                ('idPromisedPayment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='accountingList.promisedPayment', verbose_name='Обещанный платеж')),
            ],
        ),
    ]
