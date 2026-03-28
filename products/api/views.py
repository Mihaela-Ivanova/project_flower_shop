from rest_framework import generics, permissions
from products.models import Flower
from .serializers import FlowerSerializer


class FlowerListAPI(generics.ListAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [permissions.AllowAny]


class FlowerDetailAPI(generics.RetrieveAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [permissions.AllowAny]