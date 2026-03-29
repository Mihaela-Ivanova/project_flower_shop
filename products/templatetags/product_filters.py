from django import template

register = template.Library()

@register.filter
def price_with_currency(value):
    """
    Formats a decimal price with 2 digits and adds BGN currency.
    Example: 12.5 → "12.50 лв."
    """
    try:
        return f"{float(value):.2f} лв."
    except (ValueError, TypeError):
        return value