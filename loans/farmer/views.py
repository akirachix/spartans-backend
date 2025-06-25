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


