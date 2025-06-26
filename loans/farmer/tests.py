
from django.test import TestCase
from rest_framework.exceptions import ValidationError
from django.utils import timezone
# from .serializers import FarmerSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from farmer.models import Farmer, FarmerWealth


class FarmerWealthAPITestCase(APITestCase):
    def setUp(self):
        # Create Farmer instance first
        self.farmer = Farmer.objects.create(
            join_date="2025-01-01",
            status="active",
            email="wealthfarmer@example.com",
            phone_number="1234567890"
        )
        # Create FarmerWealth instance
        self.farmer_wealth = FarmerWealth.objects.create(
            farmer=self.farmer,
            milk_quantity="100 liters",
            income="5000.00"
        )
        self.list_url = reverse('farmer_wealth-list')
        self.detail_url = reverse('farmer_wealth-detail', args=[self.farmer_wealth.farmer_wealth_id])

    def test_get_farmer_wealth_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_farmer_wealth_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['milk_quantity'], self.farmer_wealth.milk_quantity)

    def test_create_farmer_wealth(self):
        data = {
            "farmer": self.farmer.farmer_id,
            "milk_quantity": "150 liters",
            "income": "7500.00"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FarmerWealth.objects.count(), 2)
        self.assertEqual(FarmerWealth.objects.last().milk_quantity, data['milk_quantity'])

    def test_update_farmer_wealth(self):
        data = {
            "farmer": self.farmer.farmer_id,
            "milk_quantity": "200 liters",
            "income": "9000.00"
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.farmer_wealth.refresh_from_db()
        self.assertEqual(self.farmer_wealth.milk_quantity, "200 liters")
        self.assertEqual(str(self.farmer_wealth.income), "9000.00")

    def test_delete_farmer_wealth(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(FarmerWealth.objects.filter(farmer_wealth_id=self.farmer_wealth.farmer_wealth_id).exists())
