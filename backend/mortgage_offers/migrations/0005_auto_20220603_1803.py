# Generated by Django 3.1.6 on 2022-06-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage_offers', '0004_auto_20220603_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='rate',
        ),
        migrations.AddField(
            model_name='offer',
            name='payment_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сумма кредита, ДО'),
        ),
        migrations.AddField(
            model_name='offer',
            name='payment_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сумма кредита, ОТ'),
        ),
        migrations.AddField(
            model_name='offer',
            name='rate_max',
            field=models.FloatField(blank=True, null=True, verbose_name='Ставка, ДО'),
        ),
        migrations.AddField(
            model_name='offer',
            name='rate_min',
            field=models.FloatField(blank=True, null=True, verbose_name='Ставка, ОТ'),
        ),
        migrations.AddField(
            model_name='offer',
            name='term_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Срок ипотеки, ДО'),
        ),
        migrations.AddField(
            model_name='offer',
            name='term_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Срок ипотеки, ОТ'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='bank_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Наименование банка'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='payment',
            field=models.IntegerField(verbose_name='Платеж в месяц'),
        ),
    ]