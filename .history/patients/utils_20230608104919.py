

import uuid


def get_uuid():
    return uuid.uuid4().hex


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
