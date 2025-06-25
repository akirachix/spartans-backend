
<<<<<<< HEAD
# Create your views here.
from rest_framework import viewsets
from .models import CooperativePartnerBank
from .serializers import (CooperativePartnerBankSerializer)
class CooperativePartnerBankViewSet(viewsets.ModelViewSet):
    queryset= CooperativePartnerBank.objects.all()
    serializer_class=CooperativePartnerBankSerializer
=======
>>>>>>> 4f0891618da362996c36835b56698068c12abe0c
