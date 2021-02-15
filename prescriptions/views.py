from typing import OrderedDict
from rest_framework import viewsets
from prescriptions.models import Prescription, Clinic, Physician, Patient
from prescriptions.serializers import PrescriptionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def post_prescription(request):
    serializer = PrescriptionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        saved_prescription = serializer.save()
    prescription = Prescription.objects.get(pk=saved_prescription.pk)
    serializer = PrescriptionSerializer(prescription)
    response = build_response(serializer.data)
    return Response(response)


def build_response(data):
    response = OrderedDict()
    response['data'] = data if data else 'Not found'
    return response
