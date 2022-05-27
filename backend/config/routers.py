from rest_framework.routers import DefaultRouter

from mortgage_offers.views import OffersViewSet

router = DefaultRouter()

router.register('offer', OffersViewSet)
