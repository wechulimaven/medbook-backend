
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from .validators import validate_year, validate_kenya_numbers

from .models import PatientTable, GenderChoices, ServicesTable


class PatientTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientTable
        fields = ("patient_name", "dob", "gender", "service")
        extra_kwargs = {
            "patient_name": {
                "required": True,
                "allow_blank": False,
                "allow_null": False,
                "validators": [UniqueValidator(queryset=PatientTable.objects.all())],
            },
            "dob": {
                "required": True,
                "validators": [validate_year]
            },
            "phone": {
                "required": False,
                "validators": [validate_kenya_numbers]
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
            dob=date
        )
        return patient_obj

class PatientDetailUpdateSerializer(PatientTableSerializer):
    service_id = serializers.CharField(
        required=False, allow_blank=True, allow_null=True
    )
    gender_id = serializers.CharField(
        required=False, allow_blank=True, allow_null=True
    )
    dob = serializers.DateTimeField()
    patient_name = serializers.DecimalField(
        max_digits=10, decimal_places=4, required=False
    )
    phone = serializers.CharField(
        required=False, allow_blank=True, allow_null=True
    )

    class Meta(PatientTableSerializer.Meta):
        pass

    def update(self, instance, validated_data):
        instance.service_id = validated_data.get("service_id", instance.service_id)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.gender_id = validated_data.get(
            "gender_id", instance.gender_id
        )
        instance.patient_name = validated_data.get(
            "patient_name", instance.patient_name
        )
        instance.save()
        return instance