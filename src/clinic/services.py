from django.db.models import QuerySet

from clinic.models import About, Details, License


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
