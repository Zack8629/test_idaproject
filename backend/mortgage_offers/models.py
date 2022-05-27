from django.db import models


class Offer(models.Model):
    bank_name = models.CharField(max_length=128, verbose_name='Наименование банка')
    term_min = models.IntegerField(verbose_name='Срок ипотеки, ОТ')
    term_max = models.IntegerField(verbose_name='Срок ипотеки, ДО')
    rate_min = models.FloatField(verbose_name='Ставка, ОТ')
    rate_max = models.FloatField(verbose_name='Ставка, ДО')
    payment_min = models.IntegerField(verbose_name='Сумма кредита, ОТ')
    payment_max = models.IntegerField(verbose_name='Сумма кредита, ДО')

    def __str__(self):
        return f'{self.bank_name}'

    class Meta:
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"
