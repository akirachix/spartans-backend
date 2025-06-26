from django.db import models

# Create your models here.
USER_TYPE_CHOICES = [
    ('farmer', 'Farmer'),
    ('cooperative', 'Cooperative'),
]

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    phone_number = models.CharField(max_length=70)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    cooperative_id = models.CharField(max_length=50, blank=True, null=True)
    national_id = models.CharField(max_length=50, blank=True, null=True)
    
    def clean(self):
        if self.type == 'cooperative':
            if not self.cooperative_id:
                raise ValidationError("Cooperative ID is required for cooperatives.")
            if self.national_id:
                raise ValidationError("Cooperatives should not have a National ID.")
        elif self.type == 'farmer':
            if not self.national_id:
                raise ValidationError("National ID is required for farmers.")
            if self.cooperative_id:
                raise ValidationError("Farmers should not have a Cooperative ID.")

    def __str__(self):
        return f"{self.fullname} ({self.get_type_display()})"