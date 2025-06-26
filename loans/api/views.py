from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets
from loan_repayments.models import LoanRepayment
from .serializers import LoanRepaymentSerializer
class LoanRepaymentViewSet (viewsets.ModelViewSet):
    queryset = LoanRepayment.objects.all()
    serializer_class = LoanRepaymentSerializer



class LoanRepaymentViewSet(viewsets.ModelViewSet):
    queryset = LoanRepayment.objects.all()
    serializer_class = LoanRepaymentSerializer

    def update(self, request, *args, **kwargs):
      
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

     
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

     
        new_amount_paid = serializer.validated_data.get('amount_paid', 0.00)  # Get the new amount paid from the request

      
        instance.amount_paid += new_amount_paid
        instance.amount_remaining -= new_amount_paid

     
        if instance.due_date < timezone.now():
         
            pass

     
        instance.save()

    
        return Response(serializer.data, status=status.HTTP_200_OK)