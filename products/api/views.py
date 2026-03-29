from rest_framework import generics, permissions
from rest_framework.generics import ListAPIView

from products.models import Flower
from .serializers import FlowerSerializer


class FlowerListAPI(generics.ListAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        season = self.request.GET.get('season')
        search = self.request.GET.get('search')

        if category:
            queryset = queryset.filter(category__name__iexact=category)

        if tag:
            queryset = queryset.filter(tags__name__iexact=tag)

        if season:
            queryset = queryset.filter(blooming_season__iexact=season)

        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset

class FlowerDetailAPI(generics.RetrieveAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [permissions.AllowAny]
