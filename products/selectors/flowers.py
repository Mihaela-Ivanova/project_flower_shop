from django.shortcuts import get_object_or_404
from products.models import Flower

def get_flower_by_id(flower_id: int) -> Flower:
    return get_object_or_404(Flower, id=flower_id)

def list_all_flowers():
    return Flower.objects.all()

def search_flowers(query: str):
    return Flower.objects.filter(name__icontains=query)