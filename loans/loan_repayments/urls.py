from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import LoanRepaymentViewSet



router = DefaultRouter()
router.register(r'loan_repayments', LoanRepaymentViewSet, basename="loanrepayments")
urlpatterns = [
    path('', include(router.urls)),
   
]