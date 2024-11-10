from collections import defaultdict

from django.shortcuts import get_object_or_404
from django.db.models import Case, QuerySet, When

from staff.models import PositionChoices, Staff


def get_staff() -> QuerySet[Staff]:
    return Staff.objects.all()


def get_all_staff() -> dict[str, QuerySet[Staff]]:
    grouped_staff = defaultdict(list)
    staff_queryset = Staff.objects.annotate(
        position_order=Case(
            When(stage=PositionChoices.MANAGER, then=1),
            When(stage=PositionChoices.ADMINISTRATOR, then=2),
            When(stage=PositionChoices.MEDIC, then=3),
            When(stage=PositionChoices.JUNIOR_MEDIC, then=4),
            default=5,
        )
    ).order_by('position_order')

    for staff_member in staff_queryset:
        grouped_staff[staff_member.stage].append(staff_member)

    return dict(grouped_staff)


def get_staff_by_slug(slug: str) -> Staff:
    return get_object_or_404(Staff, slug=slug)
