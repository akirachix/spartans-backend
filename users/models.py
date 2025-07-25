from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

USER_TYPE_CHOICES = [
    ('farmer', 'Farmer'),
    ('cooperative', 'Cooperative'),
]

class UserManager(BaseUserManager):
    def create_user(self, national_id=None, fullname=None, phone_number=None, cooperative_id=None, password=None, **extra_fields):
       
        if extra_fields.get('type') == 'farmer' and not national_id:
            raise ValueError('National ID must be set for farmers')
       
        if extra_fields.get('type') == 'cooperative' and not cooperative_id:
            raise ValueError('Cooperative ID must be set for cooperatives')
        if not fullname:
            raise ValueError('Full name must be set')
        if not phone_number:
            raise ValueError('Phone number must be set')

        user = self.model(
            national_id=national_id,
            fullname=fullname,
            phone_number=phone_number,
            cooperative_id=cooperative_id,
            **extra_fields,
        )
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, national_id, fullname, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('type', 'cooperative') 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(national_id, fullname, phone_number, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(
        max_length=70,
        validators=[RegexValidator(regex=r'^[A-Za-z ]+$', message='Full name must contain only letters and spaces')]
    )
    phone_number = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(regex=r'^07\d{8}$', message='Phone number must be 10 digits starting with 07')]
    )
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    national_id = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        help_text="Required for farmers only!",
        validators=[RegexValidator(regex=r'^\d{7}$', message='National ID must be 7 digits')]
    )
    cooperative_id = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        help_text="Required for cooperatives only!",
        validators=[RegexValidator(regex=r'^COOP-\d{4}-\d{4}$', message='Cooperative ID must be in format COOP-XXXX-XXXX')]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'national_id'
    REQUIRED_FIELDS = ['fullname', 'phone_number', 'type']

    objects = UserManager()

    def __str__(self):
        return f"{self.fullname} ({self.get_type_display()})"

    def clean(self):
        super().clean()
        if self.type == 'farmer':
            if not self.national_id:
                raise ValidationError({'national_id': "National ID is required for farmers."})
            # cooperative_id is NOT required and can be empty/null
        elif self.type == 'cooperative':
            if not self.cooperative_id:
                raise ValidationError({'cooperative_id': "Cooperative ID is required for cooperatives."})
            

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
