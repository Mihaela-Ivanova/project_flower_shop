from django.shortcuts import get_object_or_404
from products.models import Category

def list_categories():
    return Category.objects.all().order_by("name")

def get_category_by_id(category_id: int):
    return get_object_or_404(Category, id=category_id)