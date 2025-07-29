import logging

from base.services import BaseService
from products.dtos import DeleteFavoriteProductDTO
from products.exceptions.base import ProductNotFound
from products.exceptions.delete_favorite_service import (
    DeleteFavoriteProductBaseException,
    ProductNotFoundInFavoritesException,
)
from products.models import FavoriteProduct, Product

logger = logging.getLogger(__name__)


class DeleteFavoriteProductService(BaseService):
    @classmethod
    def execute(cls, dto: DeleteFavoriteProductDTO) -> None:
        try:
            try:
                product = Product.objects.get(id=dto.product_id)
            except Product.DoesNotExist:
                raise ProductNotFound()

            try:
                favorite_product = FavoriteProduct.objects.get(
                    user=dto.user, product=product
                )
            except FavoriteProduct.DoesNotExits:
                raise ProductNotFoundInFavoritesException(
                    detail=f"The product {product.name} not found in your favorites list"
                )

            favorite_product.delete()

            logger.debug(
                "Deleted product %s from favorites list of %s",
                product.name,
                dto.user.username,
            )

        except (ProductNotFound, ProductNotFoundInFavoritesException) as e:
            logger.error("DeleteFavoriteProductService error: %s", str(e))
            raise e
        except Exception as e:
            logger.error("DeleteFavoriteProductService error: %s", str(e))
            raise DeleteFavoriteProductBaseException()
