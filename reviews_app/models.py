"""Database models for business reviews."""

from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    """Represent a customer's review of a business user."""

    business_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_reviews",
    )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="written_reviews",
    )
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Define database constraints for reviews."""

        constraints = [
            models.UniqueConstraint(
                fields=["business_user", "reviewer"],
                name="unique_business_reviewer",
            ),
        ]

    def __str__(self):
        """Return the reviewer and rating."""
        return f"{self.reviewer.username} - {self.rating}/5"
