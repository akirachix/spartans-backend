
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount_requested', models.DecimalField(decimal_places=2, max_digits=12)),
                ('amount_approved', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('purpose', models.CharField(choices=[('production', 'Production'), ('equipment', 'Equipment'), ('top-up', 'Top-up'), ('other', 'Other')], default='production', max_length=20)),
                ('status', models.CharField(choices=[('pending_approval', 'Pending Approval'), ('approved', 'Approved'), ('disbursed', 'Disbursed'), ('repaying', 'Repaying'), ('fully_paid', 'Fully Paid'), ('rejected', 'Rejected'), ('cancelled', 'Cancelled')], default='pending_approval', max_length=20)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('approval_date', models.DateTimeField(blank=True, null=True)),
                ('disbursement_date', models.DateTimeField(blank=True, null=True)),
                ('current_outstanding_balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('credit_score_at_application', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('payment_deadline', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-application_date'],
            },
        ),
    ]
