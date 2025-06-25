
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CooperativeViewSet


router = DefaultRouter()
router.register(r"cooperatives",CooperativeViewSet,basename ="cooperatives")
urlpatterns=[
    path("",include(router.urls)),
    
]

