from django.db.models import Case, QuerySet, When
from django.shortcuts import get_object_or_404

from clinic.models import (
    About,
    Contact,
    Details,
    License,
    Media,
    Policy,
    PositionChoices,
    Review,
    Staff,
)


def get_clinic_requisites() -> QuerySet[Details]:
    try:
        return Details.objects.first()
    except Exception:
        return None


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


def get_clinic_license_by_slug(slug: str) -> QuerySet[License]:
    return get_object_or_404(License, slug=slug, published=True)


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
