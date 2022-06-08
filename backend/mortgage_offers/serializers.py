from rest_framework import serializers

from mortgage_offers.models import Offer


class OffersModelSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        representation = super().to_representation(obj)
        params = self.context.get('params')

        if 'price' and 'deposit' and 'term' in params:
            try:
                price = int(params.get('price'))
                deposit = int(params.get('deposit'))
                term = int(params.get('term'))

            except ValueError as e:
                print(f'to_representation > ValueError -> {e}')

            except TypeError as e:
                print(f'to_representation > TypeError -> {e}')

            except Exception as e:
                print(f'to_representation > Exception -> {e}')

            else:
                payment = obj.calc_payment(price, deposit, term)
                representation['payment'] = payment

        if representation['payment'] is None:
            representation['payment'] = 0
        return representation

    class Meta:
        model = Offer
        fields = '__all__'
