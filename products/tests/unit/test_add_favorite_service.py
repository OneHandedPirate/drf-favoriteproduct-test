import uuid

from django.contrib.auth import get_user_model
from django.test import TestCase

from config.env_config import env_config
from products.dtos import AddFavoriteProductDTO
from products.exceptions.add_favorite_service import (
    MaxFavoriteProductsCountReachedException,
    ProductAlreadyInFavoritesException,
)
from products.exceptions.base import ProductNotFound
from products.models import FavoriteProduct, Product
from products.services import AddFavoriteProductService

User = get_user_model()


class AddFavoriteProductServiceTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="testuser", password="securepassword"
        )

        self.product = Product.objects.create(
            name="Test Product", description="Test Description", price=123.45
        )

    def test_add_favorite_successfully(self) -> None:
        dto = AddFavoriteProductDTO(user=self.user, product_id=self.product.id)
        result = AddFavoriteProductService.execute(dto)

        self.assertEqual(
            result, "The product Test Product has been added to your favorites"
        )
        self.assertTrue(
            FavoriteProduct.objects.filter(
                user=self.user, product=self.product
            ).exists()
        )

    def test_add_existing_favorite(self) -> None:
        FavoriteProduct.objects.create(user=self.user, product=self.product)

        dto = AddFavoriteProductDTO(user=self.user, product_id=self.product.id)

        with self.assertRaises(ProductAlreadyInFavoritesException):
            AddFavoriteProductService.execute(dto)
        self.assertEqual(
            FavoriteProduct.objects.filter(
                user=self.user, product=self.product
            ).count(),
            1,
        )

    def test_add_favorite_nonexistent_product(self) -> None:
        non_existing_id = uuid.uuid4()
        dto = AddFavoriteProductDTO(user=self.user, product_id=non_existing_id)

        with self.assertRaises(ProductNotFound):
            AddFavoriteProductService.execute(dto)

    def test_add_favorite_limit_reached(self) -> None:
        max_fav: int = env_config.PRODUCTS.MAX_FAV_PER_USER

        for i in range(max_fav):
            product = Product.objects.create(
                name=f"Product {i}", description="Description", price=10.0
            )
            FavoriteProduct.objects.create(user=self.user, product=product)

        extra_product = Product.objects.create(
            name="Overflow Product", description="Extra", price=15.0
        )

        dto = AddFavoriteProductDTO(user=self.user, product_id=extra_product.id)

        with self.assertRaises(MaxFavoriteProductsCountReachedException):
            AddFavoriteProductService.execute(dto)

        self.assertFalse(
            FavoriteProduct.objects.filter(
                user=self.user, product=extra_product
            ).exists()
        )
        self.assertTrue(FavoriteProduct.objects.filter(user=self.user).count(), max_fav)
