from django.shortcuts import render
from rest_framework import viewsets
from farmer.models import Farmer, FarmerWealth
from .serializers import FarmerSerializer,FarmerWealthSerializer

class FarmerViewSet(viewsets.ModelViewSet):
   queryset = Farmer.objects.all()
   serializer_class = FarmerSerializer

class FarmerWealthViewSet(viewsets.ModelViewSet):
   queryset = FarmerWealth.objects.all()
   serializer_class= FarmerWealthSerializer