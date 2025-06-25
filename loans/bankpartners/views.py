

# Create your views here.
from rest_framework import viewsets
from .models import CooperativePartnerBank
from .serializers import (CooperativePartnerBankSerializer)
class CooperativePartnerBankViewSet(viewsets.ModelViewSet):
    queryset= CooperativePartnerBank.objects.all()
    serializer_class=CooperativePartnerBankSerializer

