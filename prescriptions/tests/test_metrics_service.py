from django.test import TestCase
from unittest.mock import patch
from prescriptions.services.metrics_api import MetricsApiService


class MetricsApiServiceTestCase(TestCase):
    def setUp(self):
        self.mock_http_call_patcher = patch(
            'requests.post')
        self.mock_http_call = self.mock_http_call_patcher.start()

    def tearDown(self):
        self.mock_http_call_patcher.stop()

    def test_metrics_api_call(self):
        self.mock_http_call.return_value.ok = True
        metrics = {
            'id': '19',
            'clinic_id': 10,
            'clinic_name': 'Clínica Um Dois Três',
            'physician_id': 15,
            'physician_name': 'Dr. José Carlos Souto',
            'physician_crm': '4dad44d3-0490-40e0-bf2a-d2d050b36136',
            'patient_id': 25,
            'patient_name': 'Fabrício Ribeiro',
            'patient_email': 'fabricio@fabriciolribeiro.com',
            'patient_phone': '16981852222'
        }
        self.mock_http_call.return_value.json.return_value = metrics

        request_body = metrics.copy()
        request_body.pop('id', None)
        response = MetricsApiService().post_metrics(request_body)

        self.assertIsNotNone(response)
