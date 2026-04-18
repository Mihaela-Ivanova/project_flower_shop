from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
)
from django.shortcuts import redirect
from django.core.exceptions import ValidationError

from products.forms import (
    OrderForm, SearchForm, ReviewForm, FlowerForm, CategoryForm
)

from products.selectors.flowers import (
    list_all_flowers, search_flowers
)
from products.selectors.reviews import list_reviews_for_product

from products.services.orders import create_order
from products.services.reviews import create_review

from products.models import Flower, Review, Category
from products.tasks import send_order_confirmation_email

class FlowerListView(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'flowers'

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            return search_flowers(query)
        return list_all_flowers()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = SearchForm(self.request.GET)
        return context
class FlowerDetailView(DetailView):
    model = Flower
    template_name = 'products/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["review_form"] = ReviewForm()
        context["reviews"] = list_reviews_for_product(self.object.id)
        return context

class FlowerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Flower
    form_class = FlowerForm
    template_name = 'products/flower_form.html'
    permission_required = 'products.add_flower'
    success_url = reverse_lazy('products')

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

    def get_success_url(self):
        return reverse('product_details', kwargs={'pk': self.object.pk})


class FlowerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
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

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "products/review_form.html"

    def form_valid(self, form):
        try:
            create_review(
                product_id=self.kwargs["pk"],
                user=self.request.user,
                rating=form.cleaned_data["rating"],
                comment=form.cleaned_data["comment"],
            )
        except ValidationError as e:
            messages.error(self.request, str(e))
            return redirect("product_details", pk=self.kwargs["pk"])

        return redirect("product_details", pk=self.kwargs["pk"])


class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "products/review_confirm_delete.html"

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse("product_details", kwargs={"pk": self.object.product.pk})

class OrderCreateView(CreateView):
    form_class = OrderForm
    template_name = 'products/order_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        flower_id = self.request.POST.get("flower")
        quantity = int(self.request.POST.get("quantity", 1))

        try:
            order = create_order(
                name=form.cleaned_data["customer_name"],
                email=form.cleaned_data["customer_email"],
                phone=form.cleaned_data["customer_phone"],
                address=form.cleaned_data["address"],
                notes=form.cleaned_data["notes"],
                flower_id=flower_id,
                quantity=quantity,
            )
        except ValidationError as e:
            messages.error(self.request, str(e))
            return redirect("order_create")

        send_order_confirmation_email.delay(
            order.customer_email,
            order.customer_name,
            order.id,
        )

        messages.success(self.request, "Вашата поръчка беше изпратена успешно!")
        return redirect("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flowers"] = Flower.objects.filter(in_stock=True)
        return context
