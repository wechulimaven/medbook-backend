from django.urls import path
from . import views 

app_name = "patients"

urlpatterns = [
    path(
        "add-patient/",
        views.CreatePatientView.as_view(),
        name="add-patient"
    ),
    path(
        "patient-detail/<str:id>",
        views.GetPatientDetail.as_view(),
        name="patient-detail"
    ),
    path(
        "update-patient-detail/<str:id>",
        views.UpdatePatientsDetailsView.as_view(),
        name="patient-detail"
    ),
]