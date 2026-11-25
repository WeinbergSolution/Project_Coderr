"""Database models for authentication and user profiles."""

from django.conf import settings
from django.db import models


class Profile(models.Model):
    """Store additional information and the role of a user."""

    class ProfileType(models.TextChoices):
        """Define the available user roles."""

        CUSTOMER = "customer", "Customer"
        BUSINESS = "business", "Business"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    type = models.CharField(
        max_length=8,
        choices=ProfileType.choices,
    )
    file = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True,
    )
    location = models.CharField(max_length=255, blank=True)
    tel = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    working_hours = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the username and profile type."""
        return f"{self.user.username} ({self.type})"
