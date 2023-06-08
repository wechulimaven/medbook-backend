from django.db import models

from utils import get_uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=get_uuid, editable=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
