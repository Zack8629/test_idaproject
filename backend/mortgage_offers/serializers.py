from rest_framework.serializers import ModelSerializer

from mortgage_offers.models import Offer


class OffersModelSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
