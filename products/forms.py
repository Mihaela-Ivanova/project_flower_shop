from django import forms
from django.core.exceptions import ValidationError

from account.models import Profile
from .models import Flower, Order, Category, OrderItem, Tag


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
    class Meta:
        model = Order
        fields = [
            'customer_name',
            'customer_email',
            'customer_phone',
            'address',
            'notes',
        ]
        widgets = {
            'customer_email': forms.EmailInput(attrs={'readonly': 'readonly'}),
        }

    def clean_customer_name(self):
        name = self.cleaned_data.get('customer_name')
        if len(name) < 2:
            raise ValidationError("The name must be at least 2 characters long.")
        return name

    def clean_customer_phone(self):
        phone = self.cleaned_data.get('customer_phone')
        if not phone.isdigit():
            raise ValidationError("Please enter a valid phone number.")
        return phone

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

class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=50,
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Search flowers...',
            'class': 'form-control'
        })
    )


class ReviewForm(forms.Form):
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        label="Rating",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    comment = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your review...',
            'class': 'form-control',
            'rows': 3
        })
    )

class ProfileForm(forms.ModelForm):
    class ProfileForm(forms.ModelForm):
        email = forms.EmailField(disabled=True)

        class Meta:
            model = Profile
            fields = ['first_name',
                      'last_name',
                      'phone_number',
                      'city',
                      'address']
            labels = {
                'first_name': 'First Name',
                'last_name': 'Last Name',
                'phone_number': 'Phone Number',
                'city': 'City',
                'address': 'Address',
            }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['flower', 'quantity']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tag name'}),
            'slug': forms.TextInput(attrs={'placeholder': 'tag-slug'}),
        }
