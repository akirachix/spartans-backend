from django.db import models
from farmer.models import Farmer

# Create your models here.
from farmer.models import Farmer
class FarmerWealth(models.Model):
    farmer_wealth_id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    milk_quantity = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Wealth Record {self.farmer_wealth_id} - Farmer: {self.farmer.farmer_id}"      