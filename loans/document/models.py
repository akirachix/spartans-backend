from django.db import models
# from farmer.models import Farmer
# Create your models here.
class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
  
    type = models.TextField()
    # file_url = models.ImageField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Document {self.document_id} - Type: {self.type}"