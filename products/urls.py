from django.urls import path
from .views import (
    product_list,
    product_details,
    flower_create,
    flower_edit,
    flower_delete,
    category_list,
    category_create,
    category_edit,
    category_delete,
    order_create,
)

urlpatterns = [
    path('', product_list, name='products'),
    path('<int:pk>/', product_details, name='product_details'),

    path('create/', flower_create, name='flower_create'),
    path('<int:pk>/edit/', flower_edit, name='flower_edit'),
    path('<int:pk>/delete/', flower_delete, name='flower_delete'),

    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/<int:pk>/edit/', category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', category_delete, name='category_delete'),
    path('order/', order_create, name='order_create'),
]