from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class AccountVerificationEmailView(APIView):
    serializer_class = PatientTableSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = request.user
        user.send_verification_email()

        return Response(
            {
                "message": _(
                    "Verification link sent to email: {}, kindly check.".format(
                        user.email
                    )
                )
            }
        )
