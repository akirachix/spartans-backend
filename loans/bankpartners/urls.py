<<<<<<< HEAD
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import   CooperativePartnerBankViewSet

router=DefaultRouter()
router.register(r'cooperative_partner_banks',CooperativePartnerBankViewSet,basename="bankpartners")
urlpatterns=[
    path('',include(router.urls)),
    
]
=======

>>>>>>> 4f0891618da362996c36835b56698068c12abe0c
