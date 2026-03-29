from django.contrib import admin
from .models import Flower, Category, Order, OrderItem, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    inlines = [OrderItemInline]

admin.site.register(OrderItem)