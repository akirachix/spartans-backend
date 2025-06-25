from django.urls import path, include


from . import views
from rest_framework.routers import DefaultRouter
from .views import  FarmerWealthViewSet


router = DefaultRouter()
router.register(r'farmer_wealth',FarmerWealthViewSet,basename="farmer_wealth")


urlpatterns =[
   path('',include(router.urls)),
]
