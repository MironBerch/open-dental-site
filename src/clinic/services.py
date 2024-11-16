from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from clinic.models import About, Details, License, Contact, Media


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


def get_clinic_contact() -> QuerySet[License]:
    return Contact.objects.first()


def get_clinic_license_by_slug(slug: str) -> QuerySet[License]:
    return get_object_or_404(License, slug=slug)


def get_clinic_media() -> QuerySet[Media]:
    return Media.objects.first()
