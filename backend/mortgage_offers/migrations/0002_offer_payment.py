# Generated by Django 3.1.6 on 2022-05-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage_offers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='payment',
            field=models.IntegerField(blank=True, null=True, verbose_name='Платеж в месяц'),
        ),
    ]