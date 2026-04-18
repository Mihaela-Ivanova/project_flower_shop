from products.models import Review

def list_reviews_for_product(product_id: int):
    return Review.objects.filter(product_id=product_id).order_by("-created_at")