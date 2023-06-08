from django.db import models

# Create your models here.

class PatientTable(models.Model):
    patient_name = models.CharField(max_length=50)
    dob = models.DateField()

    def __str__(self) -> str:
        return f"{self.patient_name} - {self.dob}"

class GenderTable(models.Model):
    gender = models.CharField(max_length=50, choices=GenderChoices.)