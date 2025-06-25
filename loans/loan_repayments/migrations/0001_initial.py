
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # ('farmer', '0001_initial'),
        # ('farmerLoan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanRepayment',
            fields=[
                ('loan_repayment_id', models.AutoField(primary_key=True, serialize=False)),
                ('due_date', models.DateTimeField()),
                ('amount_remaining', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.TextField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.farmer')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmerLoan.loan')),
            ],
        ),
    ]
