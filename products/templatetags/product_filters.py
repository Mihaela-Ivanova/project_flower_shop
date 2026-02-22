from django import template

register = template.Library()

@register.filter
def format_price(price):
    return f"{price:.2f}лв."