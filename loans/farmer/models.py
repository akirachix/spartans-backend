from django.db import models

# Create your models here.

class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    join_date = models.DateField()
    status = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Farmer {self.farmer_id} - {self.email}"



class FarmerWealth(models.Model):
    farmer_wealth_id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    milk_quantity = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Wealth Record {self.farmer_wealth_id} - Farmer: {self.farmer.farmer_id}"      

