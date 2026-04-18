from products.models import Tag

def list_tags():
    return Tag.objects.all().order_by("name")