from django.db.models import Case, Count, QuerySet, When
from django.shortcuts import get_object_or_404

from clinic.models import (
    About,
    Contact,
    License,
    Media,
    Photo,
    Policy,
    PositionChoices,
    Review,
    Service,
    ServiceGroup,
    Staff,
    Work,
)


def get_clinic_about() -> QuerySet[About]:
    try:
        return About.objects.first()
    except Exception:
        return None


def get_clinic_licenses() -> QuerySet[License]:
    return License.objects.filter(published=True)


def get_clinic_contacts() -> QuerySet[License]:
    return Contact.objects.all()


def get_clinic_contact() -> QuerySet[Contact]:
    return Contact.objects.first()


def get_clinic_media() -> QuerySet[Media]:
    return Media.objects.first()


def get_clinic_policy() -> QuerySet[Policy]:
    return Policy.objects.first()


def get_published_reviews() -> QuerySet[Review]:
    return Review.objects.filter(published=True)


def get_reviews_for_main_page() -> QuerySet[Review]:
    reviews = Review.objects.filter(published=True, rating=5).order_by('-created_at')
    return [review for review in reviews if len(review.message) < 300]


def get_staff() -> QuerySet[Staff]:
    return Staff.objects.all()


def get_all_staff() -> QuerySet[Staff]:
    return Staff.objects.filter(published=True).annotate(
        position_order=Case(
            When(stage=PositionChoices.MANAGER, then=1),
            When(stage=PositionChoices.ADMINISTRATOR, then=2),
            When(stage=PositionChoices.MEDIC, then=3),
            When(stage=PositionChoices.JUNIOR_MEDIC, then=4),
            default=5,
        )
    ).order_by('position_order')


def get_service_groups() -> QuerySet[ServiceGroup]:
    return ServiceGroup.objects.all()


def get_group_by_slug(slug: str) -> ServiceGroup:
    return get_object_or_404(ServiceGroup, slug=slug)


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


def get_works() -> QuerySet[Work]:
    return Work.objects.annotate(photo_count=Count('photos')).filter(published=True)


def get_work_by_slug(slug: str) -> Work:
    return get_object_or_404(Work, slug=slug)


def get_work_images_by_work_slug(slug: str) -> QuerySet[Photo]:
    work: Work = get_object_or_404(Work, slug=slug)
    return work.photos.all()
