from django.contrib import admin

from products.models import FavoriteProduct, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    list_display = ("product__name", "user")
    search_fields = ("user__username", "product__name")
