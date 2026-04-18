from django.shortcuts import get_object_or_404
from products.models import Order

def get_order_by_id(order_id: int):
    return get_object_or_404(Order, id=order_id)