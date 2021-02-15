from django.db import models

# Create your models here


class Clinic(models.Model):
    id = models.IntegerField(
        primary_key=True, help_text="Clinic's identification number", verbose_name="Clinic ID")


class Physician(models.Model):
    id = models.IntegerField(
        primary_key=True, help_text="Physician's identification number", verbose_name="Physician ID")


class Patient(models.Model):
    id = models.IntegerField(
        primary_key=True, help_text="Patient's identification number", verbose_name="Patient ID")


class Prescription(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    text = models.CharField(help_text="Prescription",
                            verbose_name="Prescription", max_length=100)
    date = models.DateTimeField(
        help_text="Prescription date", verbose_name="Prescription Date", auto_now=True)
