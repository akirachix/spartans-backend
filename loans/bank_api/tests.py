from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from bankpartners.models import CooperativePartnerBank
from decimal import Decimal

class CooperativePartnerBankViewSetTestCase(APITestCase):
    def setUp(self):
        self.bank_data = CooperativePartnerBank.objects.create(
            bank_name = "Test Bank",
            bank_account_number ="1234567890",
            amount_owed = Decimal('1000.00'),
            amount_paid = Decimal('200.00'),
            due_date = "2025-12-31T12:00:00Z"
         
        )
        self.list_url = reverse('bankpartners-list')

    def test_create_cooperative_partner_bank(self):
        data = {
            "bank_name": "New Bank",
            "bank_account_number": "0987654321",
            "amount_owed": "1500.00",
            "amount_paid": "300.00",
            "due_date": "2025-11-30T09:00:00Z",
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['bank_name'], "New Bank")


        expected_remaining = Decimal(data['amount_owed']) - Decimal(data['amount_paid'])
        self.assertEqual(Decimal(response.data['amount_remaining']), Decimal(expected_remaining))
