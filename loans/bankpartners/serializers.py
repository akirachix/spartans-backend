from rest_framework import serializers
from .models import  CooperativePartnerBank
class CooperativePartnerBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CooperativePartnerBank
        fields = '__all__'