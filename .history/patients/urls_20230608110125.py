from django.urls import path
from . import views 

app_name = "patients"

urlpatterns = [
        path(
        "account/transaction-pin/",
        views.TransactionPinView.as_view(),
        name="transaction-pin"
    ),
]