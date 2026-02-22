from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flower, Category
from .forms import FlowerForm, CategoryForm, OrderForm, CategoryDeleteForm


def product_list(request:HttpRequest) -> HttpResponse:
    flowers = Flower.objects.all()
    return render(request, 'products/product_list.html', {'flowers': flowers})

def product_details(request, pk):
    product = get_object_or_404(Flower, pk=pk)
    return render(request, 'products/product_details.html', {'product': product})
def flower_create(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = FlowerForm()

    return render(request, 'products/flower_form.html', {'form': form})


def flower_edit(request, pk):
    flower = get_object_or_404(Flower, pk=pk)

    if request.method == 'POST':
        form = FlowerForm(request.POST, request.FILES, instance=flower)
        if form.is_valid():
            form.save()
            return redirect('product_details', pk=pk)
    else:
        form = FlowerForm(instance=flower)

    return render(request, 'products/flower_form.html', {'form': form})


def flower_delete(request, pk):
    flower = get_object_or_404(Flower, pk=pk)

    if request.method == 'POST':
        flower.delete()
        return redirect('products')

    return render(request, 'products/flower_confirm_delete.html', {'flower': flower})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'products/category_form.html', {'form': form})


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'products/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        category.delete()
        return redirect("category_list")

    form = CategoryDeleteForm(instance=category)
    return render(request, "products/category_confirm_delete.html", {"form": form, "category": category})
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вашата поръчка беше изпратена успешно!")
            return redirect('order_create')
    else:
        form = OrderForm()

    return render(request, 'order_form.html', {'form': form})


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)