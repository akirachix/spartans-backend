

from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.TextField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                # ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.farmer')),
            ],
        ),
    ]
