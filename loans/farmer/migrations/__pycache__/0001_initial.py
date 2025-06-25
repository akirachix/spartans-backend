import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    # dependencies = [
    #     ('farmer', '0001_initial'),
        
    # ]

    operations = [
        migrations.CreateModel(
            name='FarmerWealth',
            fields=[
           ('farmer_id ', models.AutoField(primary_key=True))
           ('join_date' , models.DateTimeField())
        ('status' , models.CharField(max_length=20))
        ('email' , models.EmailField(max_length=20))
       ('phone_number' , models.CharField(max_length=20))
        ('created_at' , models.DateTimeField(auto_now_add=True))
        ('updated_at' , models.DateTimeField(auto_now=True))
            ],
        ),
    ]

