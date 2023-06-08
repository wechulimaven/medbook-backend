from django.contrib import admin
from .models import PatientTable, GenderTable, ServicesTable

# Register your models here.


admin.site.register(PatientTable)
admin.site.register(GenderChoices)
admin.site.register(ServicesTable)