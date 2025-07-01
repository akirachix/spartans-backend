from rest_framework import serializers
from farmer.models import Farmer



class FarmerWealthSerializer(serializers.ModelSerializer):
   class Meta:
       model = FarmerWealth
       fields = '__all__'