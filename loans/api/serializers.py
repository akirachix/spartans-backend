# from rest_framework import serializers
# from farmer_wealth.models import FarmerWealth


# class FarmerWealthSerializer(serializers.ModelSerializer):
#   class Meta:
#       model = FarmerWealth
#       fields = '__all__'
from rest_framework import serializers
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
