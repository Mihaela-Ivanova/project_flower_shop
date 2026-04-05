from django.urls import path
from .views import (
    FlowerListView, FlowerDetailView,
    FlowerCreateView, FlowerUpdateView, FlowerDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    OrderCreateView, TagListView, TagCreateView, TagUpdateView, TagDeleteView, ReviewCreateView, ReviewDeleteView
)

urlpatterns = [
    path('', FlowerListView.as_view(), name='products'),
    path('<int:pk>/', FlowerDetailView.as_view(), name='product_details'),

    path('create/', FlowerCreateView.as_view(), name='flower_create'),
    path('<int:pk>/edit/', FlowerUpdateView.as_view(), name='flower_edit'),
    path('<int:pk>/delete/', FlowerDeleteView.as_view(), name='flower_delete'),

    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('order/', OrderCreateView.as_view(), name='order_create'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/edit/', TagUpdateView.as_view(), name='tag-edit'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
    path('<int:pk>/review/', ReviewCreateView.as_view(), name='review_create'),
    path("review/<int:pk>/delete/", ReviewDeleteView.as_view(), name="review_delete"),

]