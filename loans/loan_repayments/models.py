from django.db import models
from farmerLoan.models import Loan
from users.models import User
from django.conf import settings

# Create your models here.
class LoanRepayment(models.Model):
    loan_repayment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    amount_remaining = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(null=True, blank=True)
    status = models.TextField()
   
  

    def __str__(self):
        return f"Repayment {self.loan_repayment_id} - Status: {self.status}"

    
