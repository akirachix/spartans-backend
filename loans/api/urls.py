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
from .import views
router = DefaultRouter()
router.register(r'loan_Repayments',views.LoanRepaymentViewSet, basename="LoanRepayments")
router.register(r'documents',DocumentViewSet,basename="documents")
router.register(r'loans', LoanViewSet, basename="loans")
urlpatterns = [
    path('', include(router.urls)),
]





