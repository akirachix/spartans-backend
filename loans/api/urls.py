from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter()
router.register(r'loan_Repayments',views.LoanRepaymentViewSet, basename="LoanRepayments")
urlpatterns = [
    path('', include(router.urls)),
]