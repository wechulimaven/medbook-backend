from django.urls import path
from . import views 

app_name = "patients"

urlpatterns = [
    path(
        "add-patient/",
        views.TransactionPinView.as_view(),
        name="transaction-pin"
    ),
]