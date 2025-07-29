from django.contrib import admin

from products.models import FavoriteProduct
from users.models import CustomUser


class FavoriteInline(admin.TabularInline):
    model = FavoriteProduct
    extra = 0


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    inlines = (FavoriteInline,)
