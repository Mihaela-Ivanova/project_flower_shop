from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Flower, Category, Tag, Review, Order, OrderItem
from account.models import Profile

class ModelTests(TestCase):
    def test_category_str(self):
        category = Category.objects.create(name="Roses")
        self.assertEqual(str(category), "Roses")

    def test_flower_str(self):
        category = Category.objects.create(name="Roses")
        flower = Flower.objects.create(
            name="Red Rose",
            price=10,
            blooming_season="Spring",
            category=category
        )
        self.assertEqual(str(flower), "Red Rose")

    def test_tag_str(self):
        tag = Tag.objects.create(name="Romantic", slug="romantic")
        self.assertEqual(str(tag), "Romantic")

    def test_review_creation(self):
        user = User.objects.create_user(username="test", password="1234")
        profile = Profile.objects.create(user=user, first_name="A", last_name="B", phone_number="123")
        category = Category.objects.create(name="Roses")
        flower = Flower.objects.create(name="Red Rose", price=10, blooming_season="Spring", category=category)

        review = Review.objects.create(flower=flower, user=user, rating=5)
        self.assertEqual(review.rating, 5)

from products.forms import FlowerForm, CategoryForm, OrderForm, ReviewForm

class FormTests(TestCase):
    def test_flower_form_valid(self):
        category = Category.objects.create(name="Roses")
        form = FlowerForm(data={
            'name': 'Tulip',
            'description': 'Nice flower',
            'price': 5,
            'blooming_season': 'Spring',
            'in_stock': True,
            'category': category.id
        })
        self.assertTrue(form.is_valid())

    def test_category_form_invalid(self):
        form = CategoryForm(data={'name': 'A', 'description': 'Hi'})
        self.assertFalse(form.is_valid())

    def test_order_form_invalid_phone(self):
        form = OrderForm(data={
            'customer_name': 'John',
            'customer_email': 'john@example.com',
            'customer_phone': 'abc',
            'address': 'Street 1'
        })
        self.assertFalse(form.is_valid())

    def test_review_form_valid(self):
        form = ReviewForm(data={'rating': 5, 'comment': 'Great!'})
        self.assertTrue(form.is_valid())

from django.urls import reverse

class ViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Roses")
        self.flower = Flower.objects.create(
            name="Red Rose",
            price=10,
            blooming_season="Spring",
            category=self.category
        )

    def test_flower_list_view(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_flower_detail_view(self):
        response = self.client.get(reverse('product_details', args=[self.flower.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Red Rose")

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)

    def test_tag_list_view(self):
        Tag.objects.create(name="Romantic", slug="romantic")
        response = self.client.get(reverse('tag-list'))
        self.assertEqual(response.status_code, 200)

from rest_framework.test import APIClient

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Roses")
        self.flower = Flower.objects.create(
            name="Red Rose",
            price=10,
            blooming_season="Spring",
            category=self.category
        )

    def test_api_flower_list(self):
        response = self.client.get('/api/flowers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_api_flower_detail(self):
        response = self.client.get(f'/api/flowers/{self.flower.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "Red Rose")

from products.templatetags.product_filters import price_with_currency

class TemplateFilterTests(TestCase):
    def test_price_with_currency(self):
        result = price_with_currency(12.5)
        self.assertEqual(result, "12.50 лв.")