<<<<<<< HEAD
from django.shortcuts import render
from rest_framework import viewsets
from .models import FarmerWealth
from .serializers import FarmerWealthSerializer
class FarmerWealthViewSet(viewsets.ModelViewSet):
   queryset = FarmerWealth.objects.all()
   serializer_class= FarmerWealthSerializer

=======
>>>>>>> 912d69cbe90a8446810f79fbccc9ec87649ed5a6

