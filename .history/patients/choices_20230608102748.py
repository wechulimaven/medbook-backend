from django.db.models import TextChoices

class GenderChoices(TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"