from django.test import TestCase
from unittest.mock import patch
from prescriptions.services.clinics_api import ClinicsApiService


class ClinicsApiServiceTestCase(TestCase):
    def setUp(self):
        self.mock_http_call_patcher = patch(
            'requests.get')
        self.mock_http_call = self.mock_http_call_patcher.start()

    def tearDown(self):
        self.mock_http_call_patcher.stop()

    def test_clinics_api_call(self):
        self.mock_http_call.return_value.ok = True
        clinic = {
            'id': '10',
            'name': 'Clínica Um Dois Três'
        }
        self.mock_http_call.return_value.json.return_value = clinic

        response = ClinicsApiService().get_clinic_by_id(10)

        self.assertIsNotNone(response)
