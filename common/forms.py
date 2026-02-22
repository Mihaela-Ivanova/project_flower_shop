from django import forms
from django.core.exceptions import ValidationError
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError("Please enter your name.")
        elif len(name) < 2:
            raise ValidationError("The name must be at least 2 characters long.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Please enter an email address.")
        elif "@" not in email:
            raise ValidationError("Please enter a valid email address.")

        first_part, second_part = email.split("@")
        if not first_part:
            raise ValidationError("Please enter a valid email address.")
        elif not second_part:
            raise ValidationError("Please enter a valid email address.")
        elif "." not in second_part:
            raise ValidationError("Please enter a valid email address.")

        _, domain = second_part.split(".")
        if len(domain) < 2:
            raise ValidationError("Please enter a valid domain.")
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise ValidationError("Please enter a message.")
        elif len(message) < 10:
            raise ValidationError("The message must be at least 10 characters long.")
        return message

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if len(subject) < 5:
            raise ValidationError("The subject must be at least 5 characters long.")
        return subject

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@mail.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }