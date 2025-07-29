from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models

from base.model_mixins import TimeStampMixin, UUIDPKMixin


class CustomUser(UUIDPKMixin, TimeStampMixin, AbstractUser):
    """User"""

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    username = models.CharField(
        verbose_name="Username",
        max_length=64,
        null=True,
        blank=True,
        unique=True,
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f"{self.pk} {self.username}"

    def save(self, *args: tuple, **kwargs: dict) -> None:
        if "pbkdf2_sha" not in self.password:  # type: ignore
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
