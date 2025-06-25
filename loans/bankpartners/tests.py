from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CooperativePartnerBank

class CooperativePartnerBankAPITests(APITestCase):
    def setUp(self):
        self.bank_data = {
            "bank_name": "Test Bank",
            "bank_account_number": "1234567890",
            "amount_owed": "1000.00",
            "amount_paid": "200.00",
            "due_date": "2025-12-31T12:00:00Z",
            "amount_remaining": "800.00"
        }
        self.bank = CooperativePartnerBank.objects.create(**self.bank_data)
        self.list_url = reverse('bankpartners-list')

    def test_list_cooperative_partner_banks(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['bank_name'], "Test Bank")

    def test_create_cooperative_partner_bank(self):
        data = {
            "bank_name": "New Bank",
            "bank_account_number": "0987654321",
            "amount_owed": "1500.00",
            "amount_paid": "300.00",
            "due_date": "2025-11-30T09:00:00Z",
            "amount_remaining": "1200.00"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CooperativePartnerBank.objects.count(), 2)
        self.assertEqual(response.data['bank_name'], "New Bank")

    def test_retrieve_cooperative_partner_bank(self):
        detail_url = reverse('bankpartners-detail', args=[self.bank.bank_partner_id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bank_partner_id'], self.bank.bank_partner_id)
        self.assertEqual(response.data['bank_name'], "Test Bank")

    def test_update_cooperative_partner_bank(self):
        detail_url = reverse('bankpartners-detail', args=[self.bank.bank_partner_id])
        updated_data = self.bank_data.copy()
        updated_data['bank_name'] = "Updated Bank"
        response = self.client.put(detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.bank.refresh_from_db()
        self.assertEqual(self.bank.bank_name, "Updated Bank")

    def test_partial_update_cooperative_partner_bank(self):
        detail_url = reverse('bankpartners-detail', args=[self.bank.bank_partner_id])
        response = self.client.patch(detail_url, {"amount_paid": "500.00"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.bank.refresh_from_db()
        self.assertEqual(str(self.bank.amount_paid), "500.00")

    def test_delete_cooperative_partner_bank(self):
        detail_url = reverse('bankpartners-detail', args=[self.bank.bank_partner_id])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CooperativePartnerBank.objects.count(), 0)