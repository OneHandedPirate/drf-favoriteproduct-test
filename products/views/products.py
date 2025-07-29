from rest_framework import generics, permissions
from rest_framework_simplejwt import authentication

from base.pagination import DefaultPagination
from products.models import Product
from products.serializers import ProductSerializer


class ListProductsApiView(generics.ListAPIView):
    """List of all products with pagination"""

    permission_classes = (permissions.AllowAny,)
    authentication_classes = (authentication.JWTAuthentication,)
    pagination_class = DefaultPagination
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by("-created_at")
