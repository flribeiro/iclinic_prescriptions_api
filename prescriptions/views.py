import logging
from typing import OrderedDict
from rest_framework import viewsets
from prescriptions.models import Prescription, Clinic, Physician, Patient
from prescriptions.serializers import PrescriptionSerializer
from prescriptions.services.clinics_api import ClinicsApiService
from prescriptions.services.physicians_api import PhysiciansApiService
from prescriptions.services.patients_api import PatientsApiService
from prescriptions.services.metrics_api import MetricsApiService
from prescriptions.errors.error_catalog import errors
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import OrderedDict


# Create a logger instance
logger = logging.getLogger(__name__)


@api_view(['POST'])
def post_prescription(request):
    serializer = PrescriptionSerializer(data=request.data)

    if serializer.is_valid():
        pre_data = serializer.initial_data

        logger.info(f"API called. Payload: {pre_data}")

        api_clinics = ClinicsApiService()
        api_physicians = PhysiciansApiService()
        api_patients = PatientsApiService()
        api_metrics = MetricsApiService()

        metrics_body_request = OrderedDict()

        clinics_response = api_clinics.get_clinic_by_id(
            pre_data['clinic']['id'])
        metrics_body_request['clinic_id'] = pre_data['clinic']['id']
        metrics_body_request['clinic_name'] = clinics_response.get('name', '')

        physicians_response = api_physicians.get_physician_by_id(
            pre_data['physician']['id'])
        if 'error' in physicians_response:
            logger.warning(
                f'Error calling Physicians API: {physicians_response}')
            return Response(physicians_response, status=status.HTTP_404_NOT_FOUND) if physicians_response['error']['code'] == "02" else Response(physicians_response, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        metrics_body_request['physician_id'] = physicians_response.get(
            'id', '')
        metrics_body_request['physician_name'] = physicians_response.get(
            'name', '')
        metrics_body_request['physician_crm'] = physicians_response.get(
            'crm', '')

        patients_response = api_patients.get_patient_by_id(
            pre_data['patient']['id'])
        if 'error' in patients_response:
            logger.warning(f'Error calling Patients API: {patients_response}')
            return Response(patients_response, status=status.HTTP_404_NOT_FOUND) if patients_response['error']['code'] == "03" else Response(patients_response, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        metrics_body_request['patient_id'] = patients_response.get('id', '')
        metrics_body_request['patient_name'] = patients_response.get(
            'name', '')
        metrics_body_request['patient_email'] = patients_response.get(
            'email', '')
        metrics_body_request['patient_phone'] = patients_response.get(
            'phone', '')

        metrics_response = api_metrics.post_metrics(metrics_body_request)

        if 'error' in metrics_response:
            logger.warning(f'Error calling Metrics API: {metrics_response}')
            return Response(metrics_response, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        saved_prescription = serializer.save()
        prescription = Prescription.objects.get(pk=saved_prescription.pk)
        serializer = PrescriptionSerializer(prescription)
        response = build_response(serializer.data)
        return Response(response)
    else:
        error = {'error': errors[1]}
        logger.warning(f'Invalid request. Error: {error}')
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


def build_response(data):
    response = OrderedDict()
    response['data'] = data if data else 'Not found'
    return response
