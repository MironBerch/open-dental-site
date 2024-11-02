from django.shortcuts import get_object_or_404
from django.db.models import QuerySet

from works.models import Work, Photo


def get_works() -> QuerySet[Work]:
    return Work.objects.filter()


def get_work_by_slug(slug: str) -> Work:
    return get_object_or_404(Work, slug=slug)


def get_work_images_by_work_slug(slug: str) -> QuerySet[Photo]:
    work: Work = get_object_or_404(Work, slug=slug)
    return work.photos.all()
