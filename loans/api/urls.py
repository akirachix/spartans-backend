# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from api.views import FarmerWealthViewSet


# router = DefaultRouter()


# router.register(r'farmer_wealth',FarmerWealthViewSet,basename="farmer_wealth")


# urlpatterns = [
#   path('', include(router.urls)),
# ]
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import  DocumentViewSet
from .views import LoanViewSet

router = DefaultRouter()
router.register(r'documents',DocumentViewSet,basename="documents")
router.register(r'loans', LoanViewSet, basename="loans")

urlpatterns = [
    path('',include(router.urls)),
   

]

