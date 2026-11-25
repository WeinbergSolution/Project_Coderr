"""Database models for offers and their service packages."""

from django.conf import settings
from django.db import models


class Offer(models.Model):
    """Represent a service offered by a business user."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="offers",
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="offer_images/",
        blank=True,
        null=True,
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the offer title."""
        return self.title


class OfferDetail(models.Model):
    """Represent an individual service package of an offer."""

    class OfferType(models.TextChoices):
        """Define the available service package types."""

        BASIC = "basic", "Basic"
        STANDARD = "standard", "Standard"
        PREMIUM = "premium", "Premium"

    offer = models.ForeignKey(
        Offer,
        on_delete=models.CASCADE,
        related_name="details",
    )
    title = models.CharField(max_length=255)
    revisions = models.IntegerField()
    delivery_time_in_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.JSONField(default=list)
    offer_type = models.CharField(
        max_length=8,
        choices=OfferType.choices,
    )

    class Meta:
        """Define database constraints for service packages."""

        constraints = [
            models.UniqueConstraint(
                fields=["offer", "offer_type"],
                name="unique_offer_package_type",
            ),
        ]

    def __str__(self):
        """Return the package title and type."""
        return f"{self.title} ({self.offer_type})"
