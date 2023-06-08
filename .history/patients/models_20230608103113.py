from django.db import models

from patients.choices import GenderChoices

# Create your models here.
class GenderTable(models.Model):
    gender = models.CharField(max_length=50, choices=GenderChoices.choices)

class PatientTable(models.Model):
    patient_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.ForeignKey(GenderTable, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.patient_name} - {self.dob}"
class ServicesTable(models.Model):
    service_name = models.CharField(max_length=50)
    service_price = models.PositiveBigIntegerField