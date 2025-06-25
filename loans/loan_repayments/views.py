from django.shortcuts import render

from rest_framework import viewsets

from .models import LoanRepayment

from .serializers import LoanRepaymentSerializer

# Create your views here.

class LoanRepaymentViewSet (viewsets.ModelViewSet):
    queryset = LoanRepayment.objects.all()
    serializer_class = LoanRepaymentSerializer