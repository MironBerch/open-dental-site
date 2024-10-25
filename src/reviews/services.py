from django.db.models import QuerySet

from reviews.models import Review


def get_published_reviews() -> QuerySet[Review]:
    return Review.objects.filter(published=True)
