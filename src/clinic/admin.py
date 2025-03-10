from django.contrib import admin
from django.utils.html import format_html

from clinic.models import About, Contact, License, Media, Policy, Review, Staff, Price, PriceGroup

admin.site.register(About)
admin.site.register(Media)
admin.site.register(Policy)
admin.site.register(PriceGroup)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cost',
        'group__name',
        'published',
    )
    list_filter = ('group__name', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rating',
        'created_at',
        'published',
    )
    list_filter = ('rating', 'published', )


@admin.register(License)
class ServiceGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', ),
    }


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'opening_hours',
        'phone_numbers',
        'email',
    )


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'fio',
        'stage',
        'published',
        'view_image',
        'roles',
    )
    list_filter = ('stage', 'published',)

    def view_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 160px; height: 230px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    view_image.short_description = 'Фото'
