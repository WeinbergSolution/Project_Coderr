"""Admin configuration for user profiles."""

from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Configure the administration of user profiles."""

    list_display = ("user", "type", "location", "created_at")
    list_filter = ("type", "created_at")
    search_fields = ("user__username", "user__email", "location")
    readonly_fields = ("created_at",)
