from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
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

    image = models.URLField(
        max_length=500,
        blank=True,
        null=True,
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
        validators=[MinLengthValidator(2)],
        error_messages={
            "max_length": "Flower name must be les then 50 characters!"
        },
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.URLField(
        max_length=500,
        blank=True,
        null=True,
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

    in_stock = models.BooleanField(default=True)

    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='flowers'
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
        through='OrderItem',
        related_name='orders'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    flower = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('order', 'flower')

    def __str__(self):
        return f"{self.quantity} x {self.flower.name}"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Flower,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )