from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from patients.serializers import PatientTableSerializer
from .models import PatientTable

# Create your views here.

class CreatePatientView(APIView):
    permission_classes = ()
    serializer_class = PatientTableSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        serialized_data = PatientTableSerializer(data)
        return Response(serialized_data.data)


def GetPatientDetail(APIView):
    permission_classes = ()
    serializer_class = PatientTableSerializer

    def get(self, request, id,  *args, **kwargs):
        user_id = request.query_params.get("id")
        user_qs = PatientTable.objects.filter(id=user_id)
        if user_qs.exists():
            serializer = self.serializer_class(user_qs.get(), many=True)
            return Response(serializer.data)
        else:
            Response({
                "status": 
            })