from django.urls import path
from . import views 

app_name = "patients"

urlpatterns = [
    path(
        "add-patient/",
        views.CreatePatientView.as_view(),
        name="add-patient"
    ),
]