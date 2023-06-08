
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.db import transaction

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
                "validators"
            },
            "gender": {
                "write_only": True,
                "required": False,
                "allow_blank": True,
                "allow_null": True,
            },
        }

    def validate(self, data):
        bank_account_number = data.get("bank_account_number")
        bank_code = data.get("bank_code")
        user_qs = User.objects.filter(
            bank_account_number__iexact=bank_account_number, bank_code__iexact=bank_code)
        if user_qs.exists():
            raise serializers.ValidationError("Bank account number has already been registered.")
        return data

    def update(self, instance, validated_data):