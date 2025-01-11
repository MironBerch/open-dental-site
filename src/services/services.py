from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from services.models import Service, ServiceGroup


def get_service_groups() -> QuerySet[ServiceGroup]:
    return ServiceGroup.objects.all()


def get_group_by_slug(slug: str) -> ServiceGroup:
    return get_object_or_404(ServiceGroup, slug=slug, published=True)


def get_services_by_group(group: ServiceGroup) -> QuerySet[Service]:
    services = Service.objects.filter(group=group, published=True)
    service_details = []
    for service in services:
        min_price = service.get_min_price()
        service_details.append(
            {
                'service': service,
                'min_price': min_price,
            },
        )
    return service_details


def get_service_by_slug(slug: str) -> tuple[Service, dict[str, list]]:
    service = get_object_or_404(Service, slug=slug, published=True)
    prices = service.prices.select_related('group').all()
    grouped_prices = {}
    for price in prices:
        group_name = price.group.name if price.group else 'Другое'
        if group_name not in grouped_prices:
            grouped_prices[group_name] = []
        grouped_prices[group_name].append(price)
    return service, grouped_prices


def get_services_by_groups() -> dict:
    service_groups = get_service_groups()
    services_by_group = {}
    for group in service_groups:
        services = get_services_by_group(group)
        if services != []:
            services_by_group[group] = services
    return services_by_group
