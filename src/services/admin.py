from django.contrib import admin

from services.models import Service, Tag

admin.site.register(Tag)
admin.site.register(Service)
