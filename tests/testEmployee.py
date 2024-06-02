import unittest
from unittest.mock import MagicMock, patch
from app import create_app
from faker import Faker

fake = Faker()

class TestEmployeesEndpoint(unittest.TestCase):
    def setUp(self):
        app = create_app('DevelopmentConfig')
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    @patch('services.employeeService.save')
    def test_create_customer(self, mock_save):
        name = fake.name()
        position = fake.job()
        mock_customer = MagicMock()
        mock_customer.id = 1
        mock_customer.name = name
        mock_customer.position = position
        mock_save.return_value = mock_customer

        payload = {
            "name": name,
            "position": position
        }

        response = self.app.post('/employees/', json=payload)

        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.json['id'], mock_customer.id)


    @patch('services.customerService.save')
    def test_missing_position_payload(self, mock_save):
        name = fake.name()
        mock_customer = MagicMock()
        mock_customer.id = 1
        mock_customer.name = name
        mock_save.return_value = mock_customer

        payload = {
            "name": name,
        }

        response = self.app.post('/employees/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('position', response.json)