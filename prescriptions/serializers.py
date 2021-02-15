from django.db.models.fields import Field
from rest_framework import serializers
from prescriptions.models import Prescription, Clinic, Physician, Patient
from datetime import datetime


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ["id"]
        extra_kwargs = {
            'id': {'validators': []},
        }


class PhysicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physician
        fields = ["id"]
        extra_kwargs = {
            'id': {'validators': []},
        }


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id"]
        extra_kwargs = {
            'id': {'validators': []},
        }


class PrescriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    clinic = ClinicSerializer()
    physician = PhysicianSerializer()
    patient = PatientSerializer()
    text = serializers.CharField(max_length=100)

    def create(self, validated_data):
        clinic_data = validated_data.pop('clinic')
        physician_data = validated_data.pop('physician')
        patient_data = validated_data.pop('patient')
        clinic, c = Clinic.objects.get_or_create(**clinic_data)
        physician, c = Physician.objects.get_or_create(**physician_data)
        patient, c = Patient.objects.get_or_create(**patient_data)
        prescription = Prescription.objects.create(
            clinic=clinic, physician=physician, patient=patient, **validated_data)
        return prescription
