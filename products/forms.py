from django import forms
from django.core.exceptions import ValidationError
from .models import Flower, Order, Category


class FlowerForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError("Please enter a name.")
        elif len(name) < 2:
            raise ValidationError("The name must be at least 2 characters long.")
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("The price must be greater than 0.")
        return price

    class Meta:
        model = Flower
        fields = ['name', 'description', 'price', 'blooming_season', 'in_stock', 'category', 'photo']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'blooming_season': 'Season',
            'in_stock': 'In Stock',
            'category': 'Category',
            'photo': 'Photo',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class OrderForm(forms.ModelForm):
    def clean_customer_name(self):
        name = self.cleaned_data.get('customer_name')
        if not name:
            raise ValidationError("Please enter a name.")
        elif len(name) < 2:
            raise ValidationError("The name must be at least 2 characters long.")
        return name

    def clean_customer_phone(self):
        phone = self.cleaned_data.get('customer_phone')
        if not phone:
            raise ValidationError("Please enter a phone number.")
        elif len(phone) < 6:
            raise ValidationError("The phone number must be at least 6 digits.")
        elif not phone.isdigit():
            raise ValidationError("Please enter a valid phone number.")
        return phone

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise ValidationError("Please enter an address.")
        elif len(address) < 5:
            raise ValidationError("The address must be at least 5 characters long.")
        return address

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if not quantity:
            raise ValidationError("Please enter a quantity.")
        elif quantity <= 0:
            raise ValidationError("Please enter a valid quantity.")
        return quantity

    def clean_products(self):
        products = self.cleaned_data.get('products')
        if not products:
            raise ValidationError("Please select at least one product.")
        return products

    def clean(self):
        phone = self.cleaned_data.get('customer_phone')
        address = self.cleaned_data.get('address')
        quantity = self.cleaned_data.get('quantity')
        products = self.cleaned_data.get('products')

        if quantity and not products:
            raise ValidationError("Please enter products.")
        elif phone and not address:
            raise ValidationError("Please enter an address.")
        return self.cleaned_data

    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone']
        widgets = {
            'customer_email': forms.EmailInput(attrs={'readonly': 'readonly'}),
        }


class CategoryForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError("Please enter a name.")
        elif len(name) < 3:
            raise ValidationError("The name must be at least 3 characters long.")
        elif Category.objects.filter(name__iexact=name).exists():
            raise ValidationError("This category already exists!")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise ValidationError("Please enter a description.")
        elif len(description) < 5:
            raise ValidationError("The description is too short.")
        return description

    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Category Name',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Roses, Tulips, Orchids...'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class CategoryDeleteForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["readonly"] = True
            field.widget.attrs["disabled"] = True
