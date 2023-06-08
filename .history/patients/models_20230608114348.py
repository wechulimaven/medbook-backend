from django.db import models
from patients.base_model import BaseModel

from patients.choices import GenderChoices

# Create your models here.
class GenderTable(BaseModel):
    gender = models.CharField(max_length=50, choices=GenderChoices.choices)

    def __str__(self) -> str:
        return f"{self.gender}"

class ServicesTable(BaseModel):
    service_name = models.CharField(max_length=50)
    service_price = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.service_name} - {self.service_price}"

class PatientTable(BaseModel):
    patient_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.OneToOneField(GenderTable, on_delete=models.CASCADE, blank=True, null=True, unique=fals)
    service = models.OneToOneField(ServicesTable, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.patient_name} - {self.gender} - {self.service}"

    