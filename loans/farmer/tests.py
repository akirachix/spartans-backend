from django.test import TestCase
from rest_framework.exceptions import ValidationError
from .models import Farmer
from .serializers import FarmerSerializer
class FarmerSerializerTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'join_date': '2023-01-01T00:00:00Z',
            'status': 'active',
            'email': 'farmer@example.com',
            'phone_number': '1234567890',
        }
        self.farmer = Farmer.objects.create(**self.valid_data)
    def test_serializer_with_valid_data(self):
        serializer = FarmerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['email'], 'farmer@example.com')
    def test_serializer_with_invalid_data(self):
        invalid_data = {
            'join_date': 'invalid_date',
            'status': '',
            'email': 'invalid_email',
            'phone_number': '1234567890',
        }
        serializer = FarmerSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('join_date', serializer.errors)
        self.assertIn('status', serializer.errors)
        self.assertIn('email', serializer.errors)
    def test_serializer_update(self):
        updated_data = {
            'join_date': '2023-06-01T00:00:00Z',
            'status': 'inactive',
            'email': 'updated@example.com',
            'phone_number': '0987654321',
        }
        serializer = FarmerSerializer(instance=self.farmer, data=updated_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_farmer = serializer.save()
        self.assertEqual(updated_farmer.status, 'inactive')
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Farmer
class FarmerViewSetTest(APITestCase):
    def setUp(self):
        self.farmer = Farmer.objects.create(
            join_date='2023-01-01T00:00:00Z',
            status='active',
            email='farmer@example.com',
            phone_number='1234567890'
        )
        self.url = reverse('farmer-list')
    def test_create_farmer(self):
        data = {
            'join_date': '2023-06-01T00:00:00Z',
            'status': 'active',
            'email': 'newfarmer@example.com',
            'phone_number': '0987654321',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Farmer.objects.count(), 2)
    def test_list_farmers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    def test_update_farmer(self):
        url = reverse('farmer-detail', args=[self.farmer.farmer_id])
        data = {
            'status': 'inactive',
            'email': 'updated@example.com',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.farmer.refresh_from_db()
        self.assertEqual(self.farmer.status, 'inactive')
    def test_delete_farmer(self):
        url = reverse('farmer-detail', args=[self.farmer.farmer_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Farmer.objects.count(), 0)
from django.urls import reverse
from django.test import SimpleTestCase
class URLTests(SimpleTestCase):
    def test_farmer_list_url(self):
        url = reverse('farmer-list')
        self.assertEqual(url, '/farmers/')
    def test_farmer_detail_url(self):
        url = reverse('farmer-detail', args=[1])
        self.assertEqual(url, '/farmers/1/')












