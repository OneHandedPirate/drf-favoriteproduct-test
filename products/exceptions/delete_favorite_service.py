from rest_framework import status
from rest_framework.exceptions import APIException


class DeleteFavoriteProductBaseException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Something went wrong while deleting product from favorites. Please, try again later."
    default_code = "delete_favorite_service_base_exception"


class ProductNotFoundInFavoritesException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "The product not found in the favorites list."
    default_code = "product_not_found_in_favorites_exception"
