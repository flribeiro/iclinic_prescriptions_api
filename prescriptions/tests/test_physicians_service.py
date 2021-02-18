from django.test import TestCase
from unittest.mock import patch
from prescriptions.services.physicians_api import PhysiciansApiService


class PhysiciansApiServiceTestCase(TestCase):
    def setUp(self):
        self.mock_http_call_patcher = patch(
            'requests.get')
        self.mock_http_call = self.mock_http_call_patcher.start()

    def tearDown(self):
        self.mock_http_call_patcher.stop()

    def test_physicians_api_call(self):
        self.mock_http_call.return_value.ok = True
        physician = {
            'id': '15',
            'name': 'Dr. José Carlos Souto',
            'crm': '4dad44d3-0490-40e0-bf2a-d2d050b36136'
        }
        self.mock_http_call.return_value.json.return_value = physician

        response = PhysiciansApiService().get_physician_by_id(15)

        self.assertIsNotNone(response)
