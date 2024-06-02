import unittest
from unittest.mock import MagicMock, patch
from app import create_app
from faker import Faker

fake = Faker()

class TestProductionEndpoint(unittest.TestCase):
    def setUp(self):
        app = create_app('DevelopmentConfig')
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    @patch('services.productionService.save')
    def test_create_customer(self, mock_save):
        name = fake.name()
        price = fake.random_number()
        quantity_produced = fake.random_number()
        date_produced = fake.date_this_century()
        mock_customer = MagicMock()
        mock_customer.id = 1
        mock_customer.name = name
        mock_customer.price = price
        mock_customer.quantity_produced = quantity_produced
        mock_customer.date_produced = date_produced


        mock_save.return_value = mock_customer

        payload = {
            "name": name,
            "price": price,
            "date produced": date_produced,
            "quantity produced": quantity_produced
        }

        response = self.app.post('/products/', json=payload)

        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.json['id'], mock_customer.id)


    @patch('services.productService.save')
    def test_missing_date_payload(self, mock_save):
        name = fake.name()
        price = fake.random_number()
        quantity_produced = fake.random_number()
        mock_customer = MagicMock()
        mock_customer.id = 1
        mock_customer.name = name
        mock_customer.price = price
        mock_customer.quantity_produced = quantity_produced


        mock_save.return_value = mock_customer

        payload = {
            "name": name,
            "price": price,
            "quantity produced": quantity_produced
        }

        response = self.app.post('/productions/', json=payload)


        self.assertEqual(response.status_code, 400)
        self.assertIn('date', response.json)