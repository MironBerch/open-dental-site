from works.models import Work
from clinic.models import License, Details, Contact
from staff.models import Staff
from services.models import ServiceGroup, Service


def get_search_results(query: str):
    staff = Staff.objects.filter(
        published=True,
        fio__icontains=query,
        information__icontains=query,
    ).values('id', 'fio', 'information')
    service_groups = ServiceGroup.objects.filter(
        name__icontains=query,
        description__icontains=query,
    ).values('id', 'name', 'description')
    services = Service.objects.filter(
        published=True,
        name__icontains=query,
        information__icontains=query,
        short_information__icontains=query,
        group__name__icontains=query,
    ).values(
        'id',
        'name',
        'short_information',
        'information',
        'group__name',
    )
