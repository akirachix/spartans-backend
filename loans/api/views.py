from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.from rest_framework import viewsets
from document.models import Document
from .serializers import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

from rest_framework import viewsets
from farmerLoan.models import Loan
from .serializers import LoanSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class=LoanSerializer