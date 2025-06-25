from rest_framework import serializers

from .models import   LoanRepayment




class LoanRepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRepayment
        fields = '__all__'