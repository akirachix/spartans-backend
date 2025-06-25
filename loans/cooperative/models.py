from django.db import models
# from django.contrib.auth.models import User

class Cooperative(models.Model):
    # user = models.ForeignKey(User, null=True,on_delete=models.PROTECT)
    officer_id = models.AutoField(primary_key=True)
    officer_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=20)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.officer_name
