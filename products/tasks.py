from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_order_confirmation_email(customer_email, customer_name, order_id):
    subject = f"Order #{order_id} Confirmation"
    message = (
        f"Hello, {customer_name}!\n\n"
        f"Thank you for your order #{order_id}.\n"
        f"Our team will contact you soon.\n\n"
        f"Best regards,\nFlower Shop"
    )

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [customer_email],
        fail_silently=False,
    )

    return f"Email sent to {customer_email}"