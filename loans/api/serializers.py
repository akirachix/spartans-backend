from rest_framework import serializers
from farmer_wealth.models import FarmerWealth


class FarmerWealthSerializer(serializers.ModelSerializer):
  class Meta:
      model = FarmerWealth
      fields = '__all__'