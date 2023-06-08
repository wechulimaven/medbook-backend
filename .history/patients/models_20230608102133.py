from django.db import models

# Create your models here.

class PatientTable(models.Model):
    patient_name = models.CharField(max_length=50)
    dob = models.DateField()

    def __