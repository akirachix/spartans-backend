# from django.shortcuts import render
# from rest_framework import viewsets
from django.contrib.auth.models import User
from farmer_wealth.models import FarmerWealth
from django.shortcuts import render
from rest_framework import viewsets
from loan_repayments.models import LoanRepayment
from .serializers import LoanRepaymentSerializer
from bankpartners.models import CooperativePartnerBank
from .serializers import FarmerWealthSerializer,CooperativePartnerBankSerializer
from rest_framework import viewsets
from farmerLoan.models import Loan
from .serializers import LoanSerializer
from users.models import User
from .serializers import UserSerializer

class FarmerWealthViewSet(viewsets.ModelViewSet):
  queryset = FarmerWealth.objects.all()
  serializer_class= FarmerWealthSerializer


class LoanRepaymentViewSet (viewsets.ModelViewSet):
    queryset = LoanRepayment.objects.all()
    serializer_class = LoanRepaymentSerializer


from document.models import Document
from .serializers import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer



class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class=LoanSerializer

class CooperativePartnerBankViewSet(viewsets.ModelViewSet):
    queryset= CooperativePartnerBank.objects.all()
    serializer_class=CooperativePartnerBankSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer
