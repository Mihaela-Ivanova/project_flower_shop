from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.shortcuts import render
from .models import Flower, Category, Order
from .forms import (
    FlowerForm, CategoryForm,
    OrderForm, CategoryDeleteForm
)

class FlowerListView(ListView):
    model = Flower
    template_name = 'products/product_list.html'
    context_object_name = 'flowers'


class FlowerDetailView(DetailView):
    model = Flower
    template_name = 'products/product_details.html'
    context_object_name = 'product'


class FlowerCreateView(PermissionRequiredMixin, CreateView):
    model = Flower
    form_class = FlowerForm
    template_name = 'products/flower_form.html'
    permission_required = 'products.add_flower'
    success_url = reverse_lazy('products')


class FlowerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Flower
    form_class = FlowerForm
    template_name = 'products/flower_form.html'
    permission_required = 'products.change_flower'

    def get_success_url(self):
        return reverse_lazy('product_details', kwargs={'pk': self.object.pk})

class FlowerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Flower
    template_name = 'products/flower_confirm_delete.html'
    permission_required = 'products.delete_flower'
    success_url = reverse_lazy('products')

class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    permission_required = 'products.add_category'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    permission_required = 'products.change_category'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    model = Category
    form_class = CategoryDeleteForm
    template_name = 'products/category_confirm_delete.html'
    permission_required = 'products.delete_category'
    success_url = reverse_lazy('category_list')

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'products/order_form.html'
    success_url = reverse_lazy('order_create')

    def form_valid(self, form):
        messages.success(self.request, "Вашата поръчка беше изпратена успешно!")
        return super().form_valid(form)

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)