# from rest_framework import serializers
from farmer_wealth.models import FarmerWealth
from rest_framework import serializers
from loan_repayments.models import LoanRepayment
from bankpartners.models import CooperativePartnerBank
from users.models import User
from farmerLoan.models import Loan 
from document.models import Document
from .disbursment import DarajaAPI

class FarmerWealthSerializer(serializers.ModelSerializer):
  class Meta:
      model = FarmerWealth
      fields = '__all__'



class LoanRepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRepayment
        fields = '__all__'



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'



class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class CooperativePartnerBankSerializer(serializers.ModelSerializer):
    amount_remaining = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = CooperativePartnerBank
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ="__all__"


class STKPushSerializer(serializers.Serializer):
  phone_number = serializers.CharField()
  amount = serializers.DecimalField(max_digits=10, decimal_places=2)
  account_reference = serializers.CharField()
  transaction_desc = serializers.CharField()

class DarajaAPISerializer(serializers.Serializer):
  class Meta:
      model = LoanRepayment
      fields = "__all__"



class STKPushView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

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

            checkout_request_id = response.get('CheckoutRequestID', None)

            user = None
            if request.user.is_authenticated:
                user = AppUser.objects.get(user=request.user)

            if checkout_request_id:

                payment = PaymentDetails.objects.create(
                    phone_number=data['phone_number'],
                    amount=data['amount'],
                    account_reference=data['account_reference'],
                    transaction_desc=data['transaction_desc'],
                    mpesa_checkout_id=checkout_request_id,
                    quantity= 1,
                    type = 'payment',
                    condition='New',
                    price=data['amount'],
                )

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)