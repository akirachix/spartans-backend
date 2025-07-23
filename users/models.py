from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
USER_TYPE_CHOICES = [
    ('farmer', 'Farmer'),
    ('cooperative', 'Cooperative'),
]
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(
        max_length=70,
        validators=[
            RegexValidator(
                regex='^[A-Za-z ]+$',
                message='Full name must contain only letters and spaces'
            )
        ]
    )
    email = models.EmailField(max_length=20)
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^07\d{8}$',
                message='Phone number must be 10 digits starting with 07'
            )
        ]
    )
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    national_id = models.IntegerField(
        max_length=50,
        blank= True,
        null=True,
        help_text=("Required for farmers only!"),
        validators=[
            RegexValidator(
                regex='^\d{7}$',
                message= ("National ID must be 16 digits")
            )
        ]
    )
    cooperative_id = models.CharField(
        max_length=50,
        blank= True,
        null=True,
        help_text=("Required for cooperatives only!"),
        validators=[
            RegexValidator(
                regex='^COOP-\d{4}-\d{4}$',
                message= ("Cooperative ID must be in format COOP-XXXX-XXXX")
            )
        ]
    )
    def __str__(self):
        return f"{self.fullname} ({self.get_type_display()})"
    
    