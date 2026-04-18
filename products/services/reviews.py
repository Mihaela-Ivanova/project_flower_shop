from django.core.exceptions import ValidationError
from products.models import Review

def create_review(*, product_id: int, user, rating: int, comment: str):
    if rating < 1 or rating > 5:
        raise ValidationError("Rating must be between 1 and 5")

    return Review.objects.create(
        product_id=product_id,
        user=user,
        rating=rating,
        comment=comment,
    )