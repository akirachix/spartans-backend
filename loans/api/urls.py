from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter()
router.register(r'loan_repayments',views.LoanRepaymentViewSet, basename="loanrepayments")
urlpatterns = [
    path('', include(router.urls)),
]