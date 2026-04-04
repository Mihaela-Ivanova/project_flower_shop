from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_contact_email(name, email, message):
    subject = f"New contact message from {name}"
    body = f"Email: {email}\n\nMessage:\n{message}"

    send_mail(
        subject,
        body,
        'noreply@flowershop.bg',
        ['your_email@example.com'],
        fail_silently=False,
    )

    return "Email sent"