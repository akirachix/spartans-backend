from rest_framework import serializers
from .models import Cooperative

class CooperativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperative
        fields ="__all__"