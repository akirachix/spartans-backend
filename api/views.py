import datetime
from django.utils import timezone
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from farmer_wealth.models import FarmerWealth
from bankpartners.models import CooperativePartnerBank
from document.models import Document
from users.models import User
from loan_repayments.models import LoanRepayment
from farmerLoan.models import Loan
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import (
    LoanRepaymentSerializer,
    DocumentSerializer,
    FarmerWealthSerializer,
    CooperativePartnerBankSerializer,
    LoanSerializer,
    UserSerializer,
    DarajaAPISerializer,
    STKPushSerializer,
    LoginSerializer,
)
from .disbursment import DarajaAPI
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegisterSerializer


class FarmerWealthViewSet(viewsets.ModelViewSet):
    queryset = FarmerWealth.objects.all()
    serializer_class = FarmerWealthSerializer


class LoanRepaymentViewSet(viewsets.ModelViewSet):
    queryset = LoanRepayment.objects.all()
    serializer_class = LoanRepaymentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class CooperativePartnerBankViewSet(viewsets.ModelViewSet):
    queryset = CooperativePartnerBank.objects.all()
    serializer_class = CooperativePartnerBankSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
    callback_data = request.data
    print("Daraja Callback Data:", callback_data)

    try:
        stk_callback = callback_data['Body']['stkCallback']
        checkout_request_id = stk_callback['CheckoutRequestID']
        result_code = stk_callback['ResultCode']
        result_desc = stk_callback['ResultDesc']

        print(f"CheckoutRequestID: {checkout_request_id}, ResultCode: {result_code}, ResultDesc: {result_desc}")

        if result_code == 0:
            items = stk_callback.get('CallbackMetadata', {}).get('Item', [])
            item_dict = {item['Name']: item['Value'] for item in items}
            print(f"Payment Metadata: {item_dict}")

    except Exception as e:
        print(f"Error processing Daraja callback: {e}")

    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_type': user.type}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(phone_number=phone_number)
            except User.DoesNotExist:
                return Response({'error': 'Invalid phone number or password.'}, status=status.HTTP_401_UNAUTHORIZED)
            if user.check_password(password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user_type': user.type}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid phone number or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
