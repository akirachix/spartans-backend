from django.test import TestCase

# Create your tests here.
# tests/test_models.py

from django.test import TestCase
from farmerLoan.models import Loan
from django.utils import timezone

class LoanModelTest(TestCase):

    def setUp(self):
        """Create a Loan instance for testing."""
        self.loan = Loan.objects.create(
            amount_requested=10000.00,
            amount_approved=8000.00,
            purpose="Purchase of farming equipment",
            status="Approved",
            application_date=timezone.now(),
            approval_date=timezone.now(),
            disbursement_date=timezone.now()
        )

    def test_loan_creation(self):
        
        self.assertEqual(self.loan.amount_requested, 10000.00)
        self.assertEqual(self.loan.amount_approved, 8000.00)
        self.assertEqual(self.loan.purpose, "Purchase of farming equipment")
        self.assertEqual(self.loan.status, "Approved")

    def test_str_method(self):
        
        self.assertEqual(str(self.loan), f"Loan {self.loan.loan_id} - Status: {self.loan.status}")

    def test_dates(self):
       
        self.assertIsNotNone(self.loan.application_date)
        self.assertIsNotNone(self.loan.approval_date)
        self.assertIsNotNone(self.loan.disbursement_date)

