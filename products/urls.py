from django.urls import path

from products.views import (
    AddProductApiView,
    DeleteFavoriteProductApiView,
    ListFavoriteProductsApiView,
    ListProductsApiView,
)

urlpatterns = [
    path("", ListProductsApiView.as_view(), name="list_products"),
    path(
        "<uuid:product_id>/add-to-favorites/",
        AddProductApiView.as_view(),
        name="add_to_favorites",
    ),
    path(
        "<uuid:product_id>/remove-from-favorites/",
        DeleteFavoriteProductApiView.as_view(),
        name="remove_from_favorites",
    ),
    path("favorites/", ListFavoriteProductsApiView.as_view(), name="list_favorites"),
]
