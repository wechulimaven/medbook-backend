from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from datetime import datetime

class ValidateMobileNumber:

    def __init__(self, user, number) -> None:
        self.country = user.country
        self.phone = number

    def validate_phone(self):
        if self.country == "NG":
            return self.__check_nigeria_numbers(self.phone)
        elif self.country == "GH":
            return self.__check_ghana_numbers(self.phone)
        elif self.country == "KE":
            return self.__check_kenya_numbers(self.phone)

    def __check_ghana_numbers(self, value):
        if value and value[:3] != "233":
            raise serializers.ValidationError(_("Number must be in the format 233xxxxxxxxx"))

        if value and len(value) != 12:
            raise serializers.ValidationError(_("Number must be 12 digits - including phone code"))

        return value

    def __check_kenya_numbers(self, value):
        if value and value[:3] != "254":
            raise serializers.ValidationError(_("Number must be in the format 254xxxxxxxxx"))

        if value and len(value) != 12:
            raise serializers.ValidationError(_("Number must be 12 digits - including phone code"))

        return value

    def __check_nigeria_numbers(self, value):
        if value and len(value) != 11:
            raise serializers.ValidationError(_("Number must be 11 digits"))

        if value and value[0] != "0":
            raise serializers.ValidationError(_("Number must be in the format 0xxxxxxxxxx"))

        return "234" + value[1:]


def validate_year(value):
    year = value.year
    today_year = datetime.now().year
    if today_year - year < 0:
        raise serializers.ValidationError("year cannot be greater {today_year}".format(today_year=today_year))
    if today_year - year < 18:
        raise serializers.ValidationError("must be greater than 18")
