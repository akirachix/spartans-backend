from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets
from loan_repayments.models import LoanRepayment
from .serializers import LoanRepaymentSerializer
class LoanRepaymentViewSet (viewsets.ModelViewSet):
    queryset = LoanRepayment.objects.all()
    serializer_class = LoanRepaymentSerializer