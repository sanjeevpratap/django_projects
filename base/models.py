from django.db import models
import uuid


class BaseModel(models.Mode1):
    uid = models.UUIDField(primary_key=True, editable=False, dafault=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_add=True)

    class Meta:
        abstract = True

