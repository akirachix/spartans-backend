from rest_framework import serializers
from .models import  FarmerWealth
class FarmerWealthSerializer(serializers.ModelSerializer):
   class Meta:
       model = FarmerWealth
       fields = '__all__'