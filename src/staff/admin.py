from django.contrib import admin
from django.utils.html import format_html

from staff.models import Role, Staff

admin.site.register(Role)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('fio', ),
    }
    list_display = (
        'fio',
        'display_roles',
        'stage',
        'published',
        'view_image',
    )
    list_filter = (
        'stage',
        'published',
        'roles',
    )

    def display_roles(self, object):
        return ', '.join(role.name for role in object.roles.all())

    display_roles.short_description = 'Роли'

    def view_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: 75px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    view_image.short_description = 'Фото'
