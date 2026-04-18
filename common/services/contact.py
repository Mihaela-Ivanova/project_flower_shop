from common.models import ContactMessage
from django.core.exceptions import ValidationError
from common.tasks import send_contact_email

def create_contact_message(*, name: str, email: str, subject: str, message: str) -> ContactMessage:
    if len(name) < 2:
        raise ValidationError("Името е твърде кратко.")

    contact = ContactMessage.objects.create(
        name=name,
        email=email,
        subject=subject,
        message=message,
    )

    send_contact_email.delay(name, email, message)

    return contact