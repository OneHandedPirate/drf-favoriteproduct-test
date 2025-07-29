import logging

from base.services import BaseService
from config.env_config import env_config
from products.dtos import AddFavoriteProductDTO
from products.exceptions.add_favorite_service import (
    AddFavoriteProductBaseException,
    MaxFavoriteProductsCountReachedException,
    ProductAlreadyInFavoritesException,
)
from products.exceptions.base import ProductNotFound
from products.models import FavoriteProduct, Product

logger = logging.getLogger(__name__)


class AddFavoriteProductService(BaseService):
    @classmethod
    def execute(cls, dto: AddFavoriteProductDTO) -> str:
        try:
            try:
                product = Product.objects.get(id=dto.product_id)
            except Product.DoesNotExist:
                raise ProductNotFound()

            already_exists = FavoriteProduct.objects.filter(
                user=dto.user, product=product
            ).exists()

            if (
                not already_exists
                and FavoriteProduct.objects.filter(user=dto.user).count()
                >= env_config.PRODUCTS.MAX_FAV_PER_USER
            ):
                raise MaxFavoriteProductsCountReachedException()

            if already_exists:
                raise ProductAlreadyInFavoritesException()

            FavoriteProduct.objects.create(user=dto.user, product=product)

            logger.debug(
                "User %s added product %s to favorites", dto.user.username, product.name
            )
            return f"The product {product.name} has been added to your favorites"

        except (
            ProductNotFound,
            ProductAlreadyInFavoritesException,
            MaxFavoriteProductsCountReachedException,
        ) as e:
            logger.error("AddFavoriteProductService error: %s", str(e))
            raise e

        except Exception as e:
            logger.error("AddFavoriteProductService error: %s", str(e))
            raise AddFavoriteProductBaseException()
