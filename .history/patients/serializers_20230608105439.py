
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.db import transaction

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
            raise serializers.ValidationError("Bank account number has already been registered.")
        user_qs = User.objects.filter(
            bank_account_number__iexact=bank_account_number, bank_code__iexact=bank_code)
        if user_qs.exists():
            
        return data

    def update(self, instance, validated_data):