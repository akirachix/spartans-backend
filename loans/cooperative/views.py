from django.shortcuts import render
# from .models import Cooperative, Loan, Document, LoanRepayment, FarmerWealth, CooperativePartnerBank
# from .forms import (CooperativeForm, LoanForm, DocumentForm, 
#                     LoanRepaymentForm, FarmerWealthForm, CooperativePartnerBankForm)

# # Create your views here.
# def cooperative_list(request):
#     cooperatives = Cooperative.objects.all()
#     return render(request, 'cooperative_list.html', {'cooperatives': cooperatives})

# def cooperative_create(request):
#     if request.method == 'POST':
#         form = CooperativeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('cooperative_list')
#     else:
#         form = CooperativeForm()
#     return render(request, 'cooperative_form.html', {'form': form})

# def cooperative_update(request, officer_id):
#     cooperative = get_object_or_404(Cooperative, officer_id=officer_id)
#     if request.method == 'POST':
#         form = CooperativeForm(request.POST, instance=cooperative)
#         if form.is_valid():
#             form.save()
#             return redirect('cooperative_list')
#     else:
#         form = CooperativeForm(instance=cooperative)
#     return render(request, 'cooperative_form.html', {'form': form})

# def cooperative_delete(request, officer_id):
#     cooperative = get_object_or_404(Cooperative, officer_id=officer_id)
#     if request.method == 'POST':
#         cooperative.delete()
#         return redirect('cooperative_list')
#     return render(request, 'cooperative_confirm_delete.html', {'cooperative': cooperative})