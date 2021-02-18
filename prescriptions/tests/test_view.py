import json
from django.test import TestCase, Client
from unittest.mock import patch


class PostPrescription(TestCase):
    def setUp(self):
        self.sample_body_request = {
            'clinic': {
                'id': 10
            },
            'physician': {
                'id': 15
            },
            'patient': {
                'id': 25
            },
            'text': 'Xarope XPTO 2x ao dia'
        }

        self.mock_get_clinic_patcher = patch(
            'prescriptions.services.clinics_api.ClinicsApiService.get_clinic_by_id')
        self.mock_get_clinic = self.mock_get_clinic_patcher.start()
        self.mock_get_physician_patcher = patch(
            'prescriptions.services.physicians_api.PhysiciansApiService.get_physician_by_id')
        self.mock_get_physician = self.mock_get_physician_patcher.start()
        self.mock_get_patient_patcher = patch(
            'prescriptions.services.patients_api.PatientsApiService.get_patient_by_id')
        self.mock_get_patient = self.mock_get_patient_patcher.start()
        self.mock_post_metrics_patcher = patch(
            'prescriptions.services.metrics_api.MetricsApiService.post_metrics')
        self.mock_post_metrics = self.mock_post_metrics_patcher.start()

    def tearDown(self):
        self.mock_get_clinic_patcher.stop()
        self.mock_get_physician_patcher.stop()
        self.mock_get_patient_patcher.stop()

    def test_post_api(self):
        self.mock_get_clinic.return_value.ok = True
        clinic = {
            'id': '10',
            'name': 'Clínica Um Dois Três'
        }
        self.mock_get_clinic.return_value.json.return_value = clinic

        self.mock_get_physician.return_value.ok = True
        physician = {
            'id': '15',
            'name': 'Dr. José Carlos Souto',
            'crm': '4dad44d3-0490-40e0-bf2a-d2d050b36136'
        }
        self.mock_get_physician.return_value.json.return_value = physician

        self.mock_get_patient.return_value.ok = True
        patient = {
            'id': '25',
            'name': 'Fabrício Ribeiro',
            'email': 'fabricio@fabriciolribeiro.com',
            'phone': '16981852222'
        }
        self.mock_get_patient.return_value.json.return_value = patient

        self.mock_post_metrics.return_value.ok = True
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
        self.mock_post_metrics.return_value.json.return_value = metrics

        client = Client()

        response = client.post(
            '/prescriptions/', data=json.dumps(self.sample_body_request), content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_post_api_clinics_fail(self):
        self.mock_get_clinic.return_value.ok = False

        self.mock_get_physician.return_value.ok = True
        physician = {
            'id': '15',
            'name': 'Dr. José Carlos Souto',
            'crm': '4dad44d3-0490-40e0-bf2a-d2d050b36136'
        }
        self.mock_get_physician.return_value.json.return_value = physician

        self.mock_get_patient.return_value.ok = True
        patient = {
            'id': '25',
            'name': 'Fabrício Ribeiro',
            'email': 'fabricio@fabriciolribeiro.com',
            'phone': '16981852222'
        }
        self.mock_get_patient.return_value.json.return_value = patient

        self.mock_post_metrics.return_value.ok = True
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
        self.mock_post_metrics.return_value.json.return_value = metrics

        client = Client()

        response = client.post(
            '/prescriptions/', data=json.dumps(self.sample_body_request), content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_post_request_payload_malformed(self):
        self.mock_get_clinic.return_value.ok = True
        clinic = {
            'id': '10',
            'name': 'Clínica Um Dois Três'
        }
        self.mock_get_clinic.return_value.json.return_value = clinic

        self.mock_get_physician.return_value.ok = True
        physician = {
            'id': '15',
            'name': 'Dr. José Carlos Souto',
            'crm': '4dad44d3-0490-40e0-bf2a-d2d050b36136'
        }
        self.mock_get_physician.return_value.json.return_value = physician

        self.mock_get_patient.return_value.ok = True
        patient = {
            'id': '25',
            'name': 'Fabrício Ribeiro',
            'email': 'fabricio@fabriciolribeiro.com',
            'phone': '16981852222'
        }
        self.mock_get_patient.return_value.json.return_value = patient

        self.mock_post_metrics.return_value.ok = True
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
        self.mock_post_metrics.return_value.json.return_value = metrics

        invalid_payload_request = {}

        client = Client()

        response = client.post(
            '/prescriptions/', data=json.dumps(invalid_payload_request), content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_post_api_physicians_fail(self):
        self.mock_get_clinic.return_value.ok = True
        clinic = {
            'id': '10',
            'name': 'Clínica Um Dois Três'
        }
        self.mock_get_clinic.return_value.json.return_value = clinic

        self.mock_get_physician.return_value.ok = False

        self.mock_get_patient.return_value.ok = True
        patient = {
            'id': '25',
            'name': 'Fabrício Ribeiro',
            'email': 'fabricio@fabriciolribeiro.com',
            'phone': '16981852222'
        }
        self.mock_get_patient.return_value.json.return_value = patient

        self.mock_post_metrics.return_value.ok = True
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
        self.mock_post_metrics.return_value.json.return_value = metrics

        client = Client()

        response = client.post(
            '/prescriptions/', data=json.dumps(self.sample_body_request), content_type='application/json')

        self.assertEqual(response.status_code, 200)
