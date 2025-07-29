import datetime
import uuid

from django.db import models


class UUIDPKMixin(models.Model):
    id: uuid.UUID = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    created_at: datetime.datetime = models.DateTimeField(
        "Created at",
        auto_now_add=True,
    )
    updated_at: datetime.datetime = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        abstract = True
