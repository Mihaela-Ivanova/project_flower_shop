from rest_framework import serializers
from products.models import Flower, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class FlowerSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Flower
        fields = [
            'id', 'name', 'description', 'price',
            'blooming_season', 'in_stock', 'photo', 'category'
        ]
