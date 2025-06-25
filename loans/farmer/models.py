from django.db import models

# Create your models here.

class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    join_date = models.DateField()
    status = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Farmer {self.farmer_id} - {self.email}"





