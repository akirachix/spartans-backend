from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from bankpartners.models import CooperativePartnerBank
from .serializers import (CooperativePartnerBankSerializer)

class CooperativePartnerBankViewSet(viewsets.ModelViewSet):
    queryset= CooperativePartnerBank.objects.all()
    serializer_class=CooperativePartnerBankSerializer
