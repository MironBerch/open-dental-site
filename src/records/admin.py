from django.contrib import admin

from records.models import CallRequest


@admin.register(CallRequest)
class CallRequestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'created_at',
        'processed',
    )
    list_filter = (
        'processed',
    )
