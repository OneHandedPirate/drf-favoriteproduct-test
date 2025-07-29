from django.db import models

from base.model_mixins import TimeStampMixin, UUIDPKMixin


class Product(UUIDPKMixin, TimeStampMixin):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name}: {self.price}"


class FavoriteProduct(UUIDPKMixin):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} | {self.product}"

    class Meta:
        unique_together = ("user", "product")
