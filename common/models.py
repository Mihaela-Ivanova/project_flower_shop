from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class ContactMessage(TimeStampedModel):
    name = models.CharField(
        max_length=50,
    )
    email = models.EmailField()
    subject = models.CharField(
        max_length=100,
    )
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"

