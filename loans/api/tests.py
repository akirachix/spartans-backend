from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from loan_repayments.models import LoanRepayment
from farmerLoan.models import Loan

class LoanRepaymentTests(APITestCase):

    def setUp(self):
        self.loan=Loan.objects.create(loan_id=1,amount_requested=500.00,amount_approved=500.00,
        purpose="Equipment loan", status= "Active", application_date="2025-03-26T05:40:50Z",approval_date="2025-03-28T05:40:50Z",
        disbursement_date="2025-03-29T05:40:50Z")

   
        self.LoanRepayment_data = {
            "loan_repayment_id": 3,
            "due_date": "2025-06-26T05:40:50Z",
            "amount_remaining": "20000.00",
            "amount_paid": "14000.00",
            "payment_date": "2025-06-26T05:41:14Z",
            "status": "Inactive",
            "loan": self.loan
        }

    def test_post_LoanRepayment(self):
        url = reverse('LoanRepayment-list')
        response = self.client.post(url, self.LoanRepayment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_LoanRepayment(self):
        LoanRepayment.objects.create(**self.LoanRepayment_data)
        url = reverse('LoanRepayment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_LoanRepayment(self):
        repayment = LoanRepayment.objects.create(**self.LoanRepayment_data)
        url = reverse('LoanRepayment-detail', args=[repayment.id])
        response = self.client.put(url, self.LoanRepayment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_LoanRepayment(self):
        repayment = LoanRepayment.objects.create(**self.LoanRepayment_data)
        url = reverse('LoanRepayment-detail', args=[repayment.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)