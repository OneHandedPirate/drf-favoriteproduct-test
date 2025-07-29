from rest_framework import status
from rest_framework.exceptions import APIException


class AddFavoriteProductBaseException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Something went wrong while adding product to favorites. Please, try again later"
    default_code = "add_favorite_base_exception"


class MaxFavoriteProductsCountReachedException(AddFavoriteProductBaseException):
    default_detail = "You have reached the maximum number of favorite products"
    default_code = "max_favorites_count_reached"


class ProductAlreadyInFavoritesException(AddFavoriteProductBaseException):
    default_detail = "The product is already in favorites"
    default_code = "product_already_in_favorites"
