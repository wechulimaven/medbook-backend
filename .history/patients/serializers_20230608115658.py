
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
        fields = ("patient_name", "dob", "gender")
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
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.display_name = validated_data.get(
            "display_name", instance.display_name
        )
        instance.country_code = validated_data.get(
            "country_code", instance.country_code
        )
        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )

        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.country = validated_data.get("country", instance.country)
        instance.bio = validated_data.get("bio", instance.bio)
        instance.business_name = validated_data.get("business_name", instance.business_name)
        instance.business_primary_location = validated_data.get(
            "business_primary_location", instance.business_primary_location)
        instance.latitude = validated_data.get("latitude", instance.latitude)
        instance.longitude = validated_data.get("longitude", instance.longitude)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.title = validated_data.get("title", instance.title)
        # instance.avatar = validated_data.get("avatar", instance.avatar)
        # instance.support_document = validated_data.get("support_document", instance.support_document)
        # instance.id_front = validated_data.get("id_front", instance.id_front)
        # instance.id_back = validated_data.get("id_back", instance.id_back)
        instance.save()
        return instance