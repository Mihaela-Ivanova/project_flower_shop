from common.models import ContactMessage

def list_contact_messages():
    return ContactMessage.objects.all().order_by("-created_at")