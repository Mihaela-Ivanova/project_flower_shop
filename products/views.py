from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.shortcuts import render, redirect
from .models import Flower, Category, Order, Tag, OrderItem, Review
from .forms import (
    FlowerForm, CategoryForm,
    OrderForm, CategoryDeleteForm, SearchForm, ReviewForm, TagForm
)
from .tasks import send_order_confirmation_email



class FlowerListView(ListView):
    model = Flower
    template_name = 'products/product_list.html'
    context_object_name = 'flowers'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context


class FlowerDetailView(DetailView):
    model = Flower
    template_name = 'products/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['reviews'] = self.object.reviews.all()
        return context

class FlowerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Flower
    form_class = FlowerForm
    template_name = 'products/flower_form.html'
    permission_required = 'products.add_flower'
    success_url = reverse_lazy('products')


class FlowerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Flower
    form_class = FlowerForm
    template_name = 'products/flower_form.html'
    permission_required = 'products.change_flower'

    def get_object(self, queryset=None):
        return super().get_object(queryset)

        return super().form_valid(form)

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
    template_name = 'products/category_confirm_delete.html'
    permission_required = 'products.delete_category'
    success_url = reverse_lazy('category_list')

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'products/order_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # 1) Създаваме Order
        order = form.save()

        # 2) Създаваме OrderItem
        flower_id = self.request.POST.get('flower')
        quantity = self.request.POST.get('quantity')

        if flower_id and quantity:
            OrderItem.objects.create(
                order=order,
                flower_id=flower_id,
                quantity=quantity
            )

        # 3) Async email
        send_order_confirmation_email.delay(
            order.customer_email,
            order.customer_name,
            order.id
        )

        messages.success(self.request, "Вашата поръчка беше изпратена успешно!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flowers'] = Flower.objects.filter(in_stock=True)
        return context

class TagListView(ListView):
    model = Tag
    template_name = 'products/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'products/tag_form.html'
    success_url = reverse_lazy('tag-list')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'products/tag_form.html'
    success_url = reverse_lazy('tag-list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'products/tag_confirm_delete.html'
    success_url = reverse_lazy('tag-list')

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "products/review_form.html"

    def form_valid(self, form):
        form.instance.product_id = self.kwargs["pk"]
        form.instance.user = self.request.user.userprofile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("product_details", kwargs={"pk": self.kwargs["pk"]})


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)