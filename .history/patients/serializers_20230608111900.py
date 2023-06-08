
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from .validators import validate_year

from .models import PatientTable, GenderChoices, ServicesTable


class PatientTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientTable
        fields = ("patient_name", "dob", "gender")
        extra_kwargs = {
            "patient_name": {
                "write_only": True,
                "required": True,
                "allow_blank": False,
                "allow_null": False,
                "validators": [UniqueValidator(queryset=PatientTable.objects.all())],
            },
            "dob": {
                "write_only": True,
                "required": True,
                "validators": [validate_year]
            },
        }

    # def validate(self, data):
        # gender = data.get("gender")
        # if gender.upper() not in GenderChoices.capitalize:
        #     raise serializers.ValidationError(_(f"Invalid gender provided. Gender must be {GenderChoices.choices}"))
        # return data

    def create(self, validated_data):
        date = validated_data.get("dob")
        gender = validated_data.get("gender")
        patient_name = validated_data.get ("patient_name")
        patient_obj = PatientTable.objects.create(
            patient_name=patient_name,
            gender=gender,
            date=date
        )
        return patient_obj
