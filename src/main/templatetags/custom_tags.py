from django import template

register = template.Library()


@register.filter
def map_stage(stage):
    stage_mapping = {
        'Руководитель': 'rukovoditeli',
        'Администратор': 'administratori',
        'Мед персонал': 'mediki',
        'Младщий мед персонал': 'assistenti'
    }
    return stage_mapping.get(stage, '')


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
