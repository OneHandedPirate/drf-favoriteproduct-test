import uuid

from django.contrib.auth import get_user_model
from django.test import TestCase

from products.dtos import DeleteFavoriteProductDTO
from products.exceptions.base import ProductNotFound
from products.exceptions.delete_favorite_service import (
    ProductNotFoundInFavoritesException,
)
from products.models import FavoriteProduct, Product
from products.services.delete_favorite_service import DeleteFavoriteProductService

User = get_user_model()


class DeleteFavoriteProductServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.product = Product.objects.create(name="Test Product", description="Test Product Description", price=100)
        self.favorite = FavoriteProduct.objects.create(
            user=self.user, product=self.product
        )

    def test_successful_deletion(self) -> None:
        dto = DeleteFavoriteProductDTO(user=self.user, product_id=self.product.id)

        DeleteFavoriteProductService.execute(dto)

        self.assertFalse(
            FavoriteProduct.objects.filter(
                user=self.user, product=self.product
            ).exists()
        )

    def test_product_not_found(self) -> None:
        non_existing_product_id = uuid.uuid4()

        dto = DeleteFavoriteProductDTO(
            user=self.user, product_id=non_existing_product_id
        )

        with self.assertRaises(ProductNotFound):
            DeleteFavoriteProductService.execute(dto)

    def test_product_not_in_favorites(self) -> None:
        new_product = Product.objects.create(name="Other Product", description="Other Product Description", price=100)
        dto = DeleteFavoriteProductDTO(user=self.user, product_id=new_product.id)

        with self.assertRaises(ProductNotFoundInFavoritesException):
            DeleteFavoriteProductService.execute(dto)
