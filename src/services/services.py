from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from services.models import Service, ServiceGroup


def get_service_groups() -> QuerySet[ServiceGroup]:
    return ServiceGroup.objects.all()


def get_group_by_slug(slug: str) -> ServiceGroup:
    return get_object_or_404(ServiceGroup, slug=slug)


def get_services_by_group(group: ServiceGroup) -> QuerySet[Service]:
    return Service.objects.filter(group=group)


def get_service_by_slug(slug: str) -> tuple[Service, dict[str, list]]:
    service = get_object_or_404(Service, slug=slug)
    prices = service.prices.select_related('group').all()
    grouped_prices = {}
    for price in prices:
        group_name = price.group.name if price.group else 'Другое'
        if group_name not in grouped_prices:
            grouped_prices[group_name] = []
        grouped_prices[group_name].append(price)
    return service, grouped_prices
