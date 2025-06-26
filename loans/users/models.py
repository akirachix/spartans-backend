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
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"