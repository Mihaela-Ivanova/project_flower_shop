from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Creates default user roles"

    def handle(self, *args, **kwargs):
        Group.objects.get_or_create(name='Store Manager')
        Group.objects.get_or_create(name='Customer')
        self.stdout.write(self.style.SUCCESS("Roles created successfully!"))