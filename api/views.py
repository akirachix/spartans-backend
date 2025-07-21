# from django.shortcuts import render
# from rest_framework import viewsets
from django.contrib.auth.models import User
from farmer_wealth.models import FarmerWealth
from bankpartners.models import CooperativePartnerBank
from document.models import Document
from users.models import User
from loan_repayments.models import LoanRepayment
from farmerLoan.models import Loan
from django.shortcuts import render
from .serializers import LoanRepaymentSerializer
from .serializers import DocumentSerializer
from .serializers import FarmerWealthSerializer,CooperativePartnerBankSerializer
from .serializers import LoanSerializer
from .serializers import UserSerializer
from .serializers import DarajaAPISerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .disbursment import DarajaAPI
from .serializers import STKPushSerializer  

class FarmerWealthViewSet(viewsets.ModelViewSet):
  queryset = FarmerWealth.objects.all()
  serializer_class= FarmerWealthSerializer


class LoanRepaymentViewSet(viewsets.ModelViewSet):
    queryset = LoanRepayment.objects.all()
    serializer_class = LoanRepaymentSerializer




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

# Reuse your serializer if applicable
class STKPushView(APIView):
    def post(self, request):
      serializer = STKPushSerializer(data=request.data)
      if serializer.is_valid():
          data = serializer.validated_data
          daraja = DarajaAPI()
          response = daraja.stk_push(
              phone_number=data['phone_number'],
              amount=data['amount'],
              account_reference=data['account_reference'],
              transaction_desc=data['transaction_desc']
          )
          return Response(response)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def daraja_callback(request):
    print("daraja Callback Data:", request.data)
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})