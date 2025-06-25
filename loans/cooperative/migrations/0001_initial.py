

from django.db import migrations, models

from django.conf import settings

import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Cooperative',
            fields=[
                ('officer_id', models.AutoField(primary_key=True, serialize=False)),
                ('officer_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
