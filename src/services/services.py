from django.db.models import QuerySet

from services.models import ServiceGroup


def get_service_groups() -> QuerySet[ServiceGroup]:
    return ServiceGroup.objects.all()
