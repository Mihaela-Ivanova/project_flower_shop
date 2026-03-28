from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def add_user_to_customers_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Customers')
        instance.groups.add(group)
