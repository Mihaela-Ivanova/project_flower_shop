from django.urls import path

from products.views import FlowerUpdateView
from .views import login_view, register_view, profile_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('profile/edit/', FlowerUpdateView.as_view(), name='profile_edit'),
]