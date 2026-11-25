"""Admin configuration for offers and service packages."""

from django.contrib import admin

from .models import Offer, OfferDetail


class OfferDetailInline(admin.TabularInline):
    """Display service packages within the offer administration."""

    model = OfferDetail
    extra = 0


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    """Configure the administration of offers."""

    list_display = ("title", "user", "created_at", "updated_at")
    search_fields = ("title", "description", "user__username")
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    inlines = (OfferDetailInline,)


@admin.register(OfferDetail)
class OfferDetailAdmin(admin.ModelAdmin):
    """Configure the administration of service packages."""

    list_display = ("title", "offer", "offer_type", "price")
    list_filter = ("offer_type",)
    search_fields = ("title", "offer__title")
