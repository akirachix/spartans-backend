from django.db import models
from farmer.models import Farmer
from cooperative.models import Cooperative



# Create your models here.
class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    officer = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    amount_approved = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.TextField()
    status = models.CharField(max_length=20)
    application_date = models.DateTimeField()
    approval_date = models.DateTimeField(null=True, blank=True)
    disbursement_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"Loan {self.loan_id} - Status: {self.status}"