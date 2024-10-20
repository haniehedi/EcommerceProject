# products/tests.py
from decimal import Decimal

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Product, Category


class ProductModelViewSetTests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.product1 = Product.objects.create(name='Smartphone', price=699.99, category=self.category)
        self.product2 = Product.objects.create(name='Laptop', price=999.99, category=self.category)

    def test_get_all_products(self):
        url = reverse('products-list')  # Use the correct URL name for the list view
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_products_by_name(self):
        url = reverse('products-list') + '?name=Smartphone'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Smartphone')

    def test_filter_products_by_price_range(self):
        url = reverse('products-list') + '?min_price=500&max_price=800'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Laptop')

    def test_order_products_by_price(self):
        url = reverse('products-list') + '?ordering=price'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Smartphone')

    def test_retrieve_single_product(self):
        url = reverse('products-detail', kwargs={'pk': self.product1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Smartphone')
        self.assertEqual(response.data['price'], '699.99')

    def test_update_single_product(self):
        url = reverse('products-detail', kwargs={'pk': self.product1.pk})
        data = {'name': 'Updated Smartphone', 'description' : 'it is a description', 'price': 749.99, 'category': self.category.pk}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_product = Product.objects.get(pk=self.product1.pk)
        self.assertEqual(updated_product.name, 'Updated Smartphone')
        # self.assertEqual(updated_product.price, '749.99')
        self.assertEqual(updated_product.price, Decimal('749.99'))

    def test_delete_single_product(self):
        url = reverse('products-detail', kwargs={'pk': self.product1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CategoryModelViewSetTests(APITestCase):

    def setUp(self):
        self.category1 = Category.objects.create(name='Electronics')
        self.category2 = Category.objects.create(name='Books')

    def test_get_all_categories(self):
        url = reverse('categories-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_categories_by_name(self):
        url = reverse('categories-list') + '?name=Electronics'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Electronics')
