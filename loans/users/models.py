from django.db import models
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
    
    
    