from django.core.validators import MinLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        validators= [
            MinLengthValidator(2),
        ],
        error_messages= {
            "unique": "The name already exists!",
            "max_length": "Category name must be les then 50 characters!"
        },
        unique=True
    )
    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name


class Flower(models.Model):
    class Season(models.TextChoices):
        SPRING = "Spring", "Spring"
        SUMMER = "Summer", "Summer"
        AUTUMN = "Autumn", "Autumn"
        WINTER = "Winter", "Winter"

    name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
        ],
        error_messages={
            "max_length": "Flower name must be les then 50 characters!"
        },
    )
    description = models.TextField(
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    photo = models.ImageField(
        upload_to='flowers/',
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="flowers",
    )

    blooming_season = models.CharField(
        max_length=10,
        choices=Season.choices,
    )

    in_stock = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
        ],
        error_messages={
            "max_length": "Customer name must be les then 50 characters!"
        },
    )
    customer_email = models.EmailField()
    customer_phone = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2),
        ],
        error_messages={
            "max_length": "Customer phone must be les then 50 characters!"
        },
    )

    address = models.CharField(
        max_length=200,
    )
    quantity = models.PositiveIntegerField(
        default=1,
    )

    products = models.ManyToManyField(
        Flower,
        related_name='orders'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )
    flower = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        default=1,
    )

    def __str__(self):
        return f"{self.quantity} x {self.flower.name}"