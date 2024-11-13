from django.contrib import admin

from clinic.models import About, Details, License, Contact

admin.site.register(About)
admin.site.register(Details)


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
