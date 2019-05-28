from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from . import models


class ProductListTests(APITestCase):
    def setUp(self):
        data = {
            'name': 'Eggs',
            'description': '''
                Bird and reptile eggs consist of a protective eggshell,
                albumen (egg white), and vitellus (egg yolk),
                contained within various thin membranes.
                The most commonly consumed eggs are chicken eggs.
                Other poultry eggs including those of duck and quail
                also are eaten.
            '''
        }
        models.Product.objects.create(**data)

    def test_create_product(self):
        """
        Ensure we can create a new product object.
        """
        url = reverse('products:list')
        data = {
            'name': 'Banana',
            'description': '''
                Bananas are one of the most widely consumed fruits in the
                world for good reason. Eating them could help lower blood
                pressure and reduce the risks of cancer and asthma.
            '''
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Product.objects.filter(name=data['name']).count(), 1)

    def test_create_same_product(self):
        """
        Ensure we cannot create a new product object with an already exisiting name.
        """
        url = reverse('products:list')
        data = {
            'name': 'Eggs',
            'description': '''
                Bird and reptile eggs consist of a protective eggshell,
                albumen (egg white), and vitellus (egg yolk),
                contained within various thin membranes.
                The most commonly consumed eggs are chicken eggs.
                Other poultry eggs including those of duck and quail
                also are eaten.
            '''
        }
        product_count_before = models.Product.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(models.Product.objects.count(), product_count_before)

    def test_list_product(self):
        """
        Ensure created product objects are returned.
        """
        url = reverse('products:list')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Eggs')
