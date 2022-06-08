from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from mortgage_offers.serializers import OffersModelSerializer
from .filters import OfferFilter
from .models import Offer


class OffersViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OffersModelSerializer
    filterset_class = OfferFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        params = request.query_params
        ordering = params.get('order')

        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'params': params})
            return self.sort_payment(ordering, serializer)

        serializer = self.get_serializer(queryset, many=True, context={'params': params})
        return self.sort_payment(ordering, serializer)

    @staticmethod
    def sort_payment(ordering, serializer):
        if ordering == '-payment':
            sorted_representation = sorted(serializer.data, key=lambda d: d.get('payment'),
                                           reverse=True)
            return Response(sorted_representation)

        elif ordering == 'payment':
            sorted_representation = sorted(serializer.data, key=lambda d: d.get('payment'),
                                           reverse=False)
            return Response(sorted_representation)

        else:
            return Response(serializer.data)
