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
