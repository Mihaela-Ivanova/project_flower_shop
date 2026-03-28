from django.urls import path
from .views import FlowerListAPI, FlowerDetailAPI

urlpatterns = [
    path('flowers/', FlowerListAPI.as_view(), name='api_flowers'),
    path('flowers/<int:pk>/', FlowerDetailAPI.as_view(), name='api_flower_details'),
]