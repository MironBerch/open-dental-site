from django.contrib import admin

from services.models import Service, ServiceGroup


@admin.register(ServiceGroup)
class ServiceGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', ),
    }


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', ),
    }
