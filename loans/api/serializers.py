# from rest_framework import serializers
from farmer_wealth.models import FarmerWealth
from rest_framework import serializers
from loan_repayments.models import LoanRepayment
from bankpartners.models import CooperativePartnerBank

class FarmerWealthSerializer(serializers.ModelSerializer):
  class Meta:
      model = FarmerWealth
      fields = '__all__'



class LoanRepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRepayment
        fields = '__all__'


  
from document.models import  Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

from rest_framework import serializers
from farmerLoan.models import  Loan 

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