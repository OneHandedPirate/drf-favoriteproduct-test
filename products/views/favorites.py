import uuid

from django.db.models import QuerySet
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework import generics, permissions, request, response, status, views
from rest_framework_simplejwt import authentication

from base.pagination import DefaultPagination
from base.serializers import DefaultResponseSerializer, EmptyResponseSerializer
from products.dtos import AddFavoriteProductDTO, DeleteFavoriteProductDTO
from products.models import FavoriteProduct, Product
from products.serializers import ProductSerializer
from products.services import AddFavoriteProductService, DeleteFavoriteProductService


@extend_schema(
    request=None,
    responses={
        201: OpenApiResponse(
            response=DefaultResponseSerializer,
            description="Created",
            examples=[
                OpenApiExample(
                    name="Success",
                    value={
                        "detail": "The product Computer has been added to your favorites"
                    },
                    response_only=True,
                )
            ],
        )
    },
)
class AddProductApiView(views.APIView):
    """Add product to favorites by id"""

    serializer_class = DefaultResponseSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)

    def post(self, req: request.Request, product_id: uuid.UUID) -> response.Response:
        dto = AddFavoriteProductDTO(product_id=product_id, user=self.request.user)

        message: str = AddFavoriteProductService.execute(dto)

        return response.Response(
            {"detail": message},
            status=status.HTTP_201_CREATED,
            content_type="application/json",
        )


class ListFavoriteProductsApiView(generics.ListAPIView):
    """List of favorite products with pagination"""

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)
    pagination_class = DefaultPagination
    serializer_class = ProductSerializer

    def get_queryset(self) -> QuerySet[Product]:
        user = self.request.user
        return Product.objects.filter(
            id__in=FavoriteProduct.objects.filter(user=user).values_list(
                "product_id", flat=True
            )
        ).order_by("-created_at")


@extend_schema(
    responses=EmptyResponseSerializer,
)
class DeleteFavoriteProductApiView(views.APIView):
    """Delete favorite product by id"""

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)

    def delete(self, req: request.Request, product_id: uuid.UUID) -> response.Response:
        dto = DeleteFavoriteProductDTO(product_id=product_id, user=self.request.user)

        DeleteFavoriteProductService.execute(dto)

        return response.Response(
            status=status.HTTP_204_NO_CONTENT,
            content_type="application/json",
        )
