from django import template

register = template.Library()


@register.filter
def rubles_formatted(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        return f'{value} рублей'

    last_digit = value % 10
    last_two_digits = value % 100

    if 11 <= last_two_digits <= 19:
        return f'{value} рублей'
    elif last_digit == 1:
        return f'{value} рубль'
    elif 2 <= last_digit <= 4:
        return f'{value} рубля'
    else:
        return f'{value} рублей'
