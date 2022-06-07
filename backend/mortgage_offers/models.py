from django.db import models


class Offer(models.Model):
    payment = models.IntegerField(verbose_name='Платеж в месяц', null=True, blank=True)
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

    def calc_payment(self, price: int, deposit: int, term: int):
        monthly_rate = self.rate_min / 12 / 100

        try:
            price = int(price)
            deposit = int(deposit)
            term = int(term)

        except ValueError as e:
            print(f'ValueError calc_payment -> {e}')

        except Exception as e:
            print(f'Exception calc_payment -> {e}')

        else:
            credit_amount = price * (1 - deposit / 100)
            term_in_months = term * 12
            total_rate = (1 + monthly_rate) ** term_in_months

            payment = credit_amount * monthly_rate * total_rate / (total_rate - 1) + 1

            return int(payment)
