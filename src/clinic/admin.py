from django.contrib import admin

from clinic.models import About, Contact, Details, License, Media, Policy, Review

admin.site.register(About)
admin.site.register(Details)
admin.site.register(Media)
admin.site.register(Policy)


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
