from django_filters import rest_framework as filters

from .models import Offer


class OfferFilter(filters.FilterSet):
    bank_name = filters.CharFilter(lookup_expr='icontains')

    ordering_fields = filters.OrderingFilter(
        fields=(
            ('id', 'id'),
            ('bank_name', 'bank_name'),
        ),

        field_labels={
            'id': 'ID Bank',
            'bank_name': 'Name Bank',
        }
    )

    class Meta:
        model = Offer
        fields = '__all__'
