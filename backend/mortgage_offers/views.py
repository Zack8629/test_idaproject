from rest_framework.viewsets import ModelViewSet

from mortgage_offers.serializers import OffersModelSerializer
from .models import Offer


class OffersViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OffersModelSerializer
