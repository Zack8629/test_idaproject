# Generated by Django 3.1.6 on 2022-05-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=128, verbose_name='Наименование банка')),
                ('term_min', models.IntegerField(verbose_name='Срок ипотеки, ОТ')),
                ('term_max', models.IntegerField(verbose_name='Срок ипотеки, ДО')),
                ('rate_min', models.FloatField(verbose_name='Ставка, ОТ')),
                ('rate_max', models.FloatField(verbose_name='Ставка, ДО')),
                ('payment_min', models.IntegerField(verbose_name='Сумма кредита, ОТ')),
                ('payment_max', models.IntegerField(verbose_name='Сумма кредита, ДО')),
            ],
            options={
                'verbose_name': 'Предложение',
                'verbose_name_plural': 'Предложения',
            },
        ),
    ]
