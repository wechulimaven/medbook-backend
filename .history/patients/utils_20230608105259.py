from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from datetime import datetime
import uuid


def get_uuid():
    return uuid.uuid4().hex

