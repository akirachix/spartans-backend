<<<<<<< HEAD
from django.shortcuts import render
from rest_framework import viewsets
from .models import Farmer
from .serializers import FarmerSerializer
class FarmerViewSet(viewsets.ModelViewSet):
   queryset = Farmer.objects.all()
   serializer_class = FarmerSerializer
=======
# from django.shortcuts import render,redirect

# # Create your views here.
# # views.py

# from .models import Farmer
# from .forms import FarmerForm


# def farmer_list(request):
#     farmers = Farmer.objects.all()
#     return render(request, 'farmer_list.html', {'farmers': farmers})

# def farmer_create(request):
#     if request.method == 'POST':
#         form = FarmerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('farmer_list')
#     else:
#         form = FarmerForm()
#     return render(request, 'farmer_form.html', {'form': form})


>>>>>>> 912d69cbe90a8446810f79fbccc9ec87649ed5a6
