from django.db import models
from users.models import User
from django.utils import timezone
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models, transaction
from django.utils import timezone
from users.models import User
from api.credit import calculate_credit_score, determine_max_loan_amount
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

CHOICE_TYPE_CHOICES = [
    ('production', 'Production'),
    ('equipment','Equipment'),
    ('top-up','Top-up'),
    ('other','Other',)
]
STATUS_CHOICES = [
    ('pending_approval', 'Pending Approval'),
    ('approved', 'Approved'),
    ('disbursed', 'Disbursed'),
    ('repaying', 'Repaying'),
    ('fully_paid', 'Fully Paid'),
    ('rejected', 'Rejected'),
    ('cancelled', 'Cancelled'),
    ]

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans',null=True) 
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    amount_approved = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    purpose = models.CharField(max_length=20, choices=CHOICE_TYPE_CHOICES, default='production')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending_approval')
    application_date = models.DateTimeField(auto_now_add=True)
    approval_date = models.DateTimeField(null=True, blank=True)
    disbursement_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-application_date']

    def __str__(self):
        return f"Loan {self.loan_id} - User: {self.user.fullname} - Status: {self.status}"

    def save(self, *args, **kwargs):

        if self.status == 'approved' and self.amount_approved is None:
            self.amount_approved = self.amount_requested
            self.current_outstanding_balance = self.amount_approved

    
        if self.current_outstanding_balance <= 0:
            self.current_outstanding_balance = 0
            if self.status != 'fully_paid':
                self.status = 'fully_paid'

        super().save(*args, **kwargs)

    def mark_as_disbursed(self):
        if self.status == 'approved':
            self.status = 'disbursed'
            self.disbursement_date = timezone.now()
            self.amount_disbursed = self.amount_approved or self.amount_requested
            self.current_outstanding_balance = self.amount_disbursed
            self.save()
            return True
        return False

    def process_payment(self, amount_paid):
        if amount_paid > 0:
            self.current_outstanding_balance -= amount_paid
            if self.current_outstanding_balance <= 0:
                self.current_outstanding_balance = 0
                self.status = 'fully_paid'
            elif self.status not in ['repaying', 'disbursed']:
                self.status = 'repaying'
            self.save()
            return True
        return False


    def _get_latest_repayment_status(self):
        latest_repayment = LoanRepayment.objects.filter(user=self.user).order_by('-due_date').first()
        if latest_repayment:
            return latest_repayment.repayment_status()
        return 'on_time'

    def _calculate_credit_score(self):
        if self.user.type != 'farmer':
            raise ValidationError("Only farmers can apply for loans.")

        livestock_number = getattr(self.user, 'livestock_number', None)
        monthly_income = getattr(self.user, 'monthly_income', None)

        if livestock_number is None or monthly_income is None:
            raise ValidationError("User must have 'livestock_number' and 'monthly_income' attributes set.")

        repayment_status = self._get_latest_repayment_status()
        max_income = 60000 

        score = calculate_credit_score(
            user=self.user,
            livestock_number=livestock_number,
            monthly_income=monthly_income,
            max_income=max_income,
            repayment_status=repayment_status
        )
        return Decimal(round(score, 2))

    def clean(self):
        if self.user.type != 'farmer':
            raise ValidationError("Only farmers can create loan applications.")

        credit_score = self._calculate_credit_score()
        self.credit_score_at_application = credit_score

        max_eligible_amount = determine_max_loan_amount(credit_score)

        if self.amount_requested > max_eligible_amount:
            raise ValidationError({
                'amount_requested': (
                    f"Requested amount {self.amount_requested} exceeds the maximum eligible loan amount "
                    f"{max_eligible_amount} for your credit score ({credit_score})."
                )
            })

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.full_clean()
        is_new = self._state.adding

        previous_status = None
        if not is_new:
            previous = LoanApplication.objects.filter(pk=self.pk).first()
            if previous:
                previous_status = previous.status

        super().save(*args, **kwargs)


        if self.status == 'approved' and previous_status != 'approved':
            loan, created = Loan.objects.get_or_create(user=self.user)
            loan.amount_requested = self.amount_requested
            loan.amount_approved = self.amount_requested
            loan.purpose = self.purpose
            loan.status = 'approved'
            loan.approval_date = timezone.now()
            loan.current_outstanding_balance = loan.amount_approved
            loan.save()

        elif self.status == 'rejected' and previous_status != 'rejected':
            Loan.objects.filter(user=self.user).update(status='cancelled')

    def __str__(self):
        return f"Loan Application {self.application_id} - User: {self.user.fullname} - Status: {self.status or 'N/A'}"


class LoanApplication(models.Model):

    def save(self, *args, **kwargs):
        self.full_clean()
        is_new = self._state.adding

        previous_status = None
        if not is_new:
            previous = LoanApplication.objects.filter(pk=self.pk).first()
            if previous:
                previous_status = previous.status

        super().save(*args, **kwargs)

        channel_layer = get_channel_layer()

        notification = {
            "type": "loan_application_notification",  
            "content": {
                "application_id": self.application_id,
                "user": self.user.fullname,
                "amount_requested": str(self.amount_requested),
                "status": self.status,
                "application_date": self.application_date.isoformat(),
            },
        }

        async_to_sync(channel_layer.group_send)("loan_applications_group", notification)
