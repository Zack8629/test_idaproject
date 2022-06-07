from django_filters import rest_framework as filters

from .models import Offer


class OfferFilter(filters.FilterSet):
    order = filters.OrderingFilter(
        fields=(
            ('rate_min', 'rate'),
            ('payment', 'payment'),
        ),

        field_labels={
            'rate_min': 'Ставка банка',
            'payment': 'Ежемесячный платеж',
        }
    )

    class Meta:
        model = Offer
        fields = ['rate_min', 'rate_max', 'payment_min', 'payment_max']
