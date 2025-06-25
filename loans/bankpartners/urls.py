
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import   CooperativePartnerBankViewSet

router=DefaultRouter()
router.register(r'cooperative_partner_banks',CooperativePartnerBankViewSet,basename="bankpartners")
urlpatterns=[
    path('',include(router.urls)),
    
]
