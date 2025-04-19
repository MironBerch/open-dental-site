import logging
from datetime import datetime

from bs4 import BeautifulSoup

from django.db.models import Count, QuerySet
from django.shortcuts import get_object_or_404

from clinic.models import (
    About,
    Contact,
    License,
    Photo,
    Policy,
    Review,
    Service,
    ServiceGroup,
    Staff,
    Work,
)

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

MONTHS = {
    'января': '01', 'февраля': '02', 'марта': '03',
    'апреля': '04', 'мая': '05', 'июня': '06',
    'июля': '07', 'августа': '08', 'сентября': '09',
    'октября': '10', 'ноября': '11', 'декабря': '12',
}


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
    return Staff.objects.filter(published=True)


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


def convert_date(date_str: str) -> str:
    parts = date_str.split()
    if len(parts) == 3:
        day, month_name, year = parts
    else:
        day, month_name = parts
        year = str(datetime.now().year)
    month = MONTHS.get(month_name, '01')
    return f'{year}-{month}-{day.zfill(2)}'


def parse_yandex_reviews(html_content: str):
    soup = BeautifulSoup(html_content, 'html.parser')
    reviews = soup.find_all('div', class_='business-reviews-card-view__review')
    Review._meta.get_field('created_at').auto_now_add = False
    for review in reviews:
        review: BeautifulSoup = review
        try:
            author_name, date, rating, review_text = None, None, None, None
            author_name = review.find('span', itemprop='name').text.strip()
            date = review.find('span', class_='business-review-view__date').text.strip()
            rating = review.find('meta', itemprop='ratingValue')['content']
            review_text = review.find('span', class_='business-review-view__body-text').text.strip()
            Review.objects.get_or_create(
                name=author_name,
                created_at=convert_date(date),
                rating=int(float(str(rating))),
                message=review_text,
            )
        except Exception as e:
            print(e)
    Review._meta.get_field('created_at').auto_now_add = True
