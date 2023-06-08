from django.urls import path
from . import views 

app_name = "patients"

urlpatterns = [
    path(
        "add",
        views.TransactionPinView.as_view(),
        name="transaction-pin"
    ),
]