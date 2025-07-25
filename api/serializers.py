
from farmer_wealth.models import FarmerWealth
from rest_framework import serializers
from loan_repayments.models import LoanRepayment
from bankpartners.models import CooperativePartnerBank
from users.models import User
from farmerLoan.models import Loan 
from loan_repayments.models import LoanRepayment
from api.credit import calculate_credit_score
from document.models import Document
from .disbursment import DarajaAPI
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from farmerLoan.models import LoanApplication
from rest_framework.exceptions import PermissionDenied
from rest_framework.validators import UniqueValidator


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


class DarajaAPISerializer(serializers.Serializer):
  class Meta:
      model = LoanRepayment
      fields = "__all__"

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
                if user:
                    if user.role == 'trader':
                        payment.trader = user
                    elif user.role == 'upcycler':
                        payment.upcycler = user
                    payment.save()

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CreditSerializer(serializers.ModelSerializer):
    credit_score = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['user_id', 'fullname', 'type', 'phone_number', 'livestock_number', 'monthly_income', 'credit_score']

    def get_credit_score(self, obj):
        if obj.type != 'farmer':
            raise PermissionDenied("User must be a farmer to access credit score.")

        max_income = 60000  

        latest_repayment = LoanRepayment.objects.filter(user=obj).order_by('-due_date').first()
        repayment_status = 'on_time'
        if latest_repayment:
            repayment_status = latest_repayment.repayment_status()

        livestock_number = getattr(obj, 'livestock_number', 1)  
        monthly_income = getattr(obj, 'monthly_income', 0)

        score = calculate_credit_score(
            user=obj,
            livestock_number=livestock_number,
            monthly_income=monthly_income,
            max_income=max_income,
            repayment_status=repayment_status
        )
        return round(score, 2)

class LoanApplicationSerializer(serializers.Serializer):
  class Meta:
      model = LoanApplication
      fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={'input_type': 'password'},
        error_messages={
            'min_length': 'Password must be at least 8 characters long.'
        }
    )
    phone_number = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="Phone number already registered.")]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="Email already registered.")]
    )
    class Meta:
        model = User
        fields = "__all__"
    def validate_type(self, value):
        allowed_types = [choice[0] for choice in User.USER_TYPE_CHOICES]
        if value not in allowed_types:
            raise serializers.ValidationError("Invalid user type.")
        return value
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  
        user.save()
        return user
class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})