from django.test import TestCase
from prescriptions.models import Prescription, Clinic, Patient, Physician


class PrescriptionTestCase(TestCase):
    def setUp(self):
        pt = Patient.objects.create(id=1)
        cl = Clinic.objects.create(id=2)
        ph = Physician.objects.create(id=3)
        Prescription.objects.create(
            id=1, clinic=cl, physician=ph, patient=pt, text="Diclofenaco Potássico 2x ao dia")

    def test_validate_prescription_data(self):
        """Validate if prescription data were correctly populated."""
        p = Prescription.objects.get(pk=1)
        self.assertTrue(isinstance(p, Prescription))
        self.assertEqual(p.patient.id, 1)
        self.assertEqual(p.clinic.id, 2)
        self.assertEqual(p.physician.id, 3)
        self.assertEquals(p.text, "Diclofenaco Potássico 2x ao dia")
