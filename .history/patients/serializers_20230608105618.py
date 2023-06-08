
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from patients.utils import validate_year

from .models import PatientTable, GenderChoices, ServicesTable


class UserBankAccountDetailsSerializer(serializers.ModelSerializer):
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
                "allow_blank": False,
                "allow_null": False,
                "validators": [validate_year]
            },
            "gender": {
                "write_only": True,
                "required": True,
                "allow_blank": False,
                "allow_null": False,
            },
        }

    def validate(self, data):
        gender = data.get("gender")
        if gender not in GenderChoices.choices:
            raise serializers.ValidationError(_("Bank account number has already been registered."))
        return data

    def create(self, validated_data):
        date = validated_data.get("date")
        date = validated_data.get("date")
        PatientTable.objects.create()
