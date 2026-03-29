from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        from django.contrib.contenttypes.models import ContentType
        from products.models import Flower, Category, Tag, Review

        # Create groups if they don't exist
        manager_group, created = Group.objects.get_or_create(name='Store Manager')
        customer_group, created = Group.objects.get_or_create(name='Customer')

        # Manager permissions
        manager_permissions = Permission.objects.filter(
            content_type__model__in=['flower', 'category', 'tag']
        )
        manager_group.permissions.set(manager_permissions)

        # Customer permissions
        customer_permissions = Permission.objects.filter(
            content_type__model__in=['order', 'review', 'profile']
        )
        customer_group.permissions.set(customer_permissions)