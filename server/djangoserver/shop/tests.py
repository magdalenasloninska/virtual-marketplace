from django.test import TestCase, Client
from django.urls import reverse

from .models import Listing, CustomUser
from .form import ListingForm


class GetAllItemCategoriesTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('get_all_item_categories')
    
    def test_get_all_item_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('categories', response.json())
        categories = response.json()['categories']
        self.assertIsInstance(categories, list)
        self.assertGreater(len(categories), 0)