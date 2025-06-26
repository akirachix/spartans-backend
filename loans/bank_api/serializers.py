from rest_framework import serializers
from bankpartners.models import  CooperativePartnerBank
class CooperativePartnerBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CooperativePartnerBank
        fields = '__all__'