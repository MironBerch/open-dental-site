from django.contrib import admin
from django.utils.html import format_html

from works.models import Work, Photo


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', ),
    }
    list_display = (
        'name',
        'published',
    )
    list_filter = ('published', )


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'work__name',
        'view_image',
    )
    list_filter = ('work__name', )

    def view_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: 75px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    view_image.short_description = 'Фото'
