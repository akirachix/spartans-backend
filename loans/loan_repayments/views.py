from rest_framework import viewsets

from .models import LoanRepayment

from .serializers import LoanRepaymentSerializer

class LoanRepaymentViewSet (viewsets.ModelViewSet):
    queryset = LoanRepayment.objects.all()
    serializer_class = LoanRepaymentSerializer
