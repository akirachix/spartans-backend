from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone
from farmer.models import Farmer  # Adjust import if needed
from .models import FarmerWealth

class FarmerWealthViewSetTests(APITestCase):
    def setUp(self):
        # Create a Farmer instance with all required fields
        self.farmer = Farmer.objects.create(
            join_date=timezone.now().date(),
            # Add other required Farmer fields here, e.g.:
            # name="Test Farmer",
            # location="Test Location",
        )

        # Create some FarmerWealth instances
        self.fw1 = FarmerWealth.objects.create(
            farmer=self.farmer,
            milk_quantity="50 liters",
            income=1000.00,
        )
        self.fw2 = FarmerWealth.objects.create(
            farmer=self.farmer,
            milk_quantity="75 liters",
            income=2000.00,
        )

        self.list_url = reverse('farmer_wealth-list')
        self.detail_url = lambda pk: reverse('farmer_wealth-detail', args=[pk])

    def test_list_farmer_wealth(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_farmer_wealth(self):
        response = self.client.get(self.detail_url(self.fw1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['farmer_wealth_id'], self.fw1.farmer_wealth_id)
        self.assertEqual(response.data['milk_quantity'], "50 liters")
        self.assertEqual(str(response.data['income']), "1000.00")

    def test_create_farmer_wealth(self):
        data = {
            'farmer': self.farmer.pk,
            'milk_quantity': "60 liters",
            'income': "1500.50",
        }
        response = self.client.post(self.list_url, data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print("Create validation errors:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FarmerWealth.objects.count(), 3)

    def test_update_farmer_wealth(self):
        data = {
            'farmer': self.farmer.pk,
            'milk_quantity': "80 liters",
            'income': "3000.00",
        }
        response = self.client.put(self.detail_url(self.fw1.pk), data, format='json')
        if response.status_code != status.HTTP_200_OK:
            print("Update validation errors:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.fw1.refresh_from_db()
        self.assertEqual(self.fw1.milk_quantity, "80 liters")
        self.assertEqual(float(self.fw1.income), 3000.00)

    def test_partial_update_farmer_wealth(self):
        data = {
            'income': "3500.00",
        }
        response = self.client.patch(self.detail_url(self.fw1.pk), data, format='json')
        if response.status_code != status.HTTP_200_OK:
            print("Partial update validation errors:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.fw1.refresh_from_db()
        self.assertEqual(float(self.fw1.income), 3500.00)

    def test_delete_farmer_wealth(self):
        response = self.client.delete(self.detail_url(self.fw1.pk))
        if response.status_code != status.HTTP_204_NO_CONTENT:
            print("Delete errors:", response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(FarmerWealth.objects.filter(pk=self.fw1.pk).exists())
