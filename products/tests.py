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


class ProductDetailTests(APITestCase):
    def setUp(self):
        data = [
            {
                'name': 'Yogurt',
                'description': '''
                    Yogurt also spelled yoghurt, yogourt or yoghourt,
                    is a food produced by bacterial fermentation of milk.
                '''
            },
            {
                'name': 'Banana',
                'description': '''
                    Bananas are one of the most widely consumed fruits in the
                    world for good reason. Eating them could help lower blood
                    pressure and reduce the risks of cancer and asthma.
                '''
            }
        ]
        for product_data in data:
            models.Product.objects.create(**product_data)

    def test_update_product(self):
        """
        Ensure we can update a product object.
        """
        data = {
            'pk': 1,
            'name': 'New yogurt',
            'description': '''
                Yogurt also spelled yoghurt, yogourt or yoghourt,
                is a food produced by bacterial fermentation of milk.
            '''
        }
        url = reverse('products:detail', kwargs={'pk': data['pk']})
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Product.objects.filter(name=data['name']).count(), 1)

    def test_update_product_unique_name(self):
        """
        Ensure we cannot change a product name to another product name.
        """
        data = {
            'pk': 1,
            'name': 'Banana',
            'description': '''
                Yogurt also spelled yoghurt, yogourt or yoghourt,
                is a food produced by bacterial fermentation of milk.
            '''
        }
        url = reverse('products:detail', kwargs={'pk': data['pk']})
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(models.Product.objects.filter(name=data['name']), data['pk'])

    def test_update_product_required_fields(self):
        """
        Ensure we cannot update a product object without a required value.
        """
        data = {
            'pk': 1,
            'name': None,
            'description': '''
                Yogurt also spelled yoghurt, yogourt or yoghourt,
                is a food produced by bacterial fermentation of milk.
            '''
        }
        url = reverse('products:detail', kwargs={'pk': data['pk']})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(models.Product.objects.filter(name=None).count(), 0)

    def test_retrieve_product(self):
        """
        Ensure we can retrieve a product object.
        """
        product_pk = 1
        url = reverse('products:detail', kwargs={'pk': product_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], product_pk)

    def test_delete_product(self):
        """
        Ensure we can delete a product object.
        """
        product_pk = 1
        product_count_before = models.Product.objects.count()
        url = reverse('products:detail', kwargs={'pk': product_pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(product_count_before - models.Product.objects.count(), 1)

    def test_delete_product_non_valid_pk(self):
        """
        Ensure we receive Not Found for a non-existing PK.
        """
        product_pk = 9999
        product_count_before = models.Product.objects.count()
        url = reverse('products:detail', kwargs={'pk': product_pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
