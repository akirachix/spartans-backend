from rest_framework import serializers
from bankpartners.models import  CooperativePartnerBank
class CooperativePartnerBankSerializer(serializers.ModelSerializer):
    amount_remaining = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = CooperativePartnerBank
        fields = '__all__'