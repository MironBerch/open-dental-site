from django.db.models import Q
from django.urls import reverse

from clinic.models import Staff
from services.models import Service, ServiceGroup
from works.models import Work


def get_search_results(query: str):
    query = query.upper()

    sites = {
        'контакты': reverse('contacts'),
        'отзывы клиентов': reverse('reviews'),
        'лицензии': reverse('licenses'),
        'услуги': reverse('services_groups'),
        'цены': reverse('prices'),
        'персонал специалисты сотрудники': reverse('staff'),
        'клиника': reverse('company'),
        'галерея наши работы': reverse('gallery'),
        'карта сайта': reverse('site_map'),
    }

    results = []

    # Staff results
    staff_results = Staff.objects.filter(published=True).filter(
        Q(fio__iregex=query) | Q(information__iregex=query)
    ).values('id', 'fio', 'information', 'slug')

    for staff in staff_results:
        match_count = (staff['fio'].lower().count(query.lower()) +
                       staff['information'].lower().count(query.lower()))
        results.append({'type': 'staff', 'match_count': match_count, 'data': staff})

    # Service Groups results
    service_group_results = ServiceGroup.objects.filter(
        Q(name__iregex=query) | Q(description__iregex=query)
    ).values('id', 'name', 'description', 'slug')

    for group in service_group_results:
        match_count = (group['name'].lower().count(query.lower()) +
                       group['description'].lower().count(query.lower()))
        results.append({'type': 'service_group', 'match_count': match_count, 'data': group})

    # Services results
    service_results = Service.objects.filter(published=True).filter(
        Q(name__iregex=query) |
        Q(information__iregex=query) |
        Q(short_information__iregex=query)
    ).values('id', 'name', 'information', 'short_information', 'slug', 'group__name', 'group__slug')

    for service in service_results:
        match_count = (service['name'].lower().count(query.lower()) +
                       service['information'].lower().count(query.lower()) +
                       service['short_information'].lower().count(query.lower()))
        results.append({'type': 'service', 'match_count': match_count, 'data': service})

    # Works results
    work_results = Work.objects.filter(published=True).filter(
        Q(name__iregex=query) | Q(information__iregex=query)
    ).values('id', 'name', 'information', 'slug')

    for work in work_results:
        match_count = (work['name'].lower().count(query.lower()) +
                       work['information'].lower().count(query.lower()))
        results.append({'type': 'work', 'match_count': match_count, 'data': work})

    # Check for Pages
    for page, url in sites.items():
        if page in query.lower():
            results.append({'type': 'page', 'match_count': 1, 'data': {'title': page, 'url': url}})

    for result in results:
        try:
            if result['type'] == 'staff':
                result['data']['url'] = reverse('staff') + f'#{result['data']['slug']}'
            if result['type'] == 'service_group':
                result['data']['url'] = reverse('services_group', args=[result['data']['slug']])
            if result['type'] == 'service':
                result['data']['url'] = reverse('service', args=[result['data']['slug']])
            if result['type'] == 'work':
                result['data']['url'] = reverse('work', args=[result['data']['slug']])
        except Exception:
            pass

    # Sort by match count (higher match count first)
    results.sort(key=lambda x: x['match_count'], reverse=True)

    return results
