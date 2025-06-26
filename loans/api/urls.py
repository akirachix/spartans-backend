# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import FarmerViewSet,FarmerWealthViewSet

router = DefaultRouter()

router.register(r'farmer', FarmerViewSet, basename="farmer")
router.register(r'farmer_wealth',FarmerWealthViewSet,basename="farmer_wealth")

urlpatterns = [
   path('', include(router.urls)),
]






