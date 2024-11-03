from django.contrib import admin

from prices.models import Price, PriceGroup

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
