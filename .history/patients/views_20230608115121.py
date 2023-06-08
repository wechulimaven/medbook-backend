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


class GetPatientDetail(APIView):
    permission_classes = ()
    serializer_class = PatientTableSerializer

    def get(self, request, id,  *args, **kwargs):
        print(f"+*****USER*** {id}")
        user_qs = PatientTable.objects.filter(id=id)
        if user_qs.exists():
            print("in here********")
            serializer = self.serializer_class(user_qs.get())
            return Response(serializer.data)
        else:
            return Response({
                "status": False,
                "message": "User does not exist"
            })


class UpdatePatientsDetailsView(APIView):
    serializer_class = PatientTableSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    def get_serializer(self,*args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)
    
    def get_patient(slef, id):
        

    def put(self, request, id, *args, **kwargs):
        
        serializer = self.get_serializer(
            instance=request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        serializer = PatientTableSerializer(user)
        print(f"User details ${serializer.data}")
        return Response(serializer.data)
