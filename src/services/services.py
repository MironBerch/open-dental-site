from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from services.models import Service, ServiceGroup


def get_service_groups() -> QuerySet[ServiceGroup]:
    return ServiceGroup.objects.all()


def get_group_by_slug(slug: str) -> ServiceGroup:
    return get_object_or_404(ServiceGroup, slug=slug)


def get_services_by_group(group: ServiceGroup) -> QuerySet[Service]:
    return Service.objects.filter(group=group)


def get_service_by_slug(slug: str) -> Service:
    return get_object_or_404(Service, slug=slug)
