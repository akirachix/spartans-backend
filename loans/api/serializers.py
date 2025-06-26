from rest_framework import serializers
from farmer.models import Farmer
from farmer.models import  FarmerWealth


class FarmerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Farmer
       fields = '__all__'

class FarmerWealthSerializer(serializers.ModelSerializer):
   class Meta:
       model = FarmerWealth
       fields = '__all__'