from rest_framework import serializers

from mortgage_offers.models import Offer


class OffersModelSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        representation = super().to_representation(obj)
        params = self.context.get('params')

        if params:
            try:
                price = int(params.get('price'))
                deposit = int(params.get('deposit'))
                term = int(params.get('term'))

            except ValueError as e:
                print(f'ValueError > serializers > to_representation -> {e}')

            except Exception as e:
                print(f'Exception > serializers > to_representation -> {e}')

            else:
                payment = obj.calc_payment(price, deposit, term)
                representation['payment'] = payment

        if representation['payment'] is None:
            # representation.pop('payment')
            representation['payment'] = 'None Type'
        return representation

    class Meta:
        model = Offer
        fields = '__all__'
