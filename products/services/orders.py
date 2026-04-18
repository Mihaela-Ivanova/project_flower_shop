from django.core.exceptions import ValidationError
from products.models import Order, OrderItem, Flower

def create_order(*, name, email, phone, address, notes, flower_id, quantity):
    if quantity <= 0:
        raise ValidationError("Quantity must be positive")

    flower = Flower.objects.get(id=flower_id)

    order = Order.objects.create(
        customer_name=name,
        customer_email=email,
        customer_phone=phone,
        address=address,
        notes=notes,
        quantity=quantity,
    )

    OrderItem.objects.create(
        order=order,
        flower=flower,
        quantity=quantity,
    )

    return order