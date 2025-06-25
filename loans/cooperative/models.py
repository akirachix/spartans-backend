from django.db import models

class Cooperative(models.Model):
    officer_id = models.AutoField(primary_key=True)
    officer_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
   
    
    def __str__(self):
        return self.officer_name

