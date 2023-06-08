from django.db import models

# Create your models here.

class PatientTable(models.Model):
    FIELDNAME = models.CharField(max_length=50)