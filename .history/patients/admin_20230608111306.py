from django.contrib import admin
from .models import PatientTable, GenderChoices, ServicesTable

# Register your models here.


admin.site.register(PatientTable)
admin.site.register(GenderChoices)
admin.site.register(ServicesTable)