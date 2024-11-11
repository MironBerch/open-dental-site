from django.db.models import Q

from works.models import Work
from clinic.models import License
from staff.models import Staff
from services.models import ServiceGroup, Service


def get_search_results(query: str):
    SITES = {
        'контакты': 'contacts',
        'отзывы клиентов': 'reviews',
        'лицензии и сертификаты': 'licenses',
        'реквизиты': 'requisites',
        'услуги': 'services_groups',
        'цены': 'prices',
        'персонал специалисты': 'staff_list',
        'клиника': 'company',
        'галерея наши работы': 'gallery',
        'карта сайта': 'site_map',
    }

    results = {
        'staff': [], 'service_groups': [], 'services': [], 'works': [], 'licenses': [], 'pages': [],
    }

    results['staff'] = list(
        Staff.objects.filter(
            published=True,
        ).filter(
            Q(fio__icontains=query) | Q(information__icontains=query),
        ).values('id', 'fio', 'information')
    )

    results['service_groups'] = list(
        ServiceGroup.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).values('id', 'name', 'description')
    )

    results['services'] = list(
        Service.objects.filter(
            published=True
        ).filter(
            Q(name__icontains=query) |
            Q(information__icontains=query) |
            Q(short_information__icontains=query),
        ).values(
            'id',
            'name',
            'short_information',
            'information',
        )
    )

    results['works'] = list(
        Work.objects.filter(published=True).filter(
            Q(name__icontains=query) | Q(information__icontains=query),
        ).values('id', 'name', 'information')
    )

    results['licenses'] = list(
        License.objects.filter(
            published=True,
            name__icontains=query,
        ).values('id', 'name')
    )

    for page, url in SITES.items():
        if page in query.lower():
            results['pages'].append({'title': page, 'url': url})

    return results
