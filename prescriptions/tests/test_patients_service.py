from django.test import TestCase
from unittest.mock import patch
from prescriptions.services.patients_api import PatientsApiService


class PatientsApiServiceTestCase(TestCase):
    def setUp(self):
        self.mock_http_call_patcher = patch(
            'requests.get')
        self.mock_http_call = self.mock_http_call_patcher.start()

    def tearDown(self):
        self.mock_http_call_patcher.stop()

    def test_patients_api_call(self):
        self.mock_http_call.return_value.ok = True
        patient = {
            'id': '25',
            'name': 'Fabrício Ribeiro',
            'email': 'fabricio@fabriciolribeiro.com',
            'phone': '16981852222'
        }
        self.mock_http_call.return_value.json.return_value = patient

        response = PatientsApiService().get_patient_by_id(25)

        self.assertIsNotNone(response)
