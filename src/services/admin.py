from django.contrib import admin

from services.models import Service, ServiceGroup

admin.site.register(ServiceGroup)
admin.site.register(Service)
