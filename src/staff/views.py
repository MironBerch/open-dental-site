from django.http import HttpRequest
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from staff.services import get_all_staff, get_staff_by_slug, get_staff_by_stage


class StaffView(TemplateResponseMixin, View):
    template_name = 'staff/list.html'

    def get(self, request: HttpRequest):
        staff = get_all_staff()
        return self.render_to_response(
            context={
                'active_page': 'staff',
                'managers':  staff.get('Руководитель', ''),
                'administrators': staff.get('Администратор', ''),
                'medics': staff.get('Мед персонал', ''),
                'junior_medics': staff.get('Младщий мед персонал', ''),
            },
        )


class StaffByStageView(TemplateResponseMixin, View):
    template_name = 'staff/stage.html'

    def get(self, request: HttpRequest, stage: str):
        staff = get_staff_by_stage(stage)
        print(staff)
        print(stage)
        return self.render_to_response(
            context={
                'page_title': 'staff[0].stage' if staff != [] else '',
                'active_page': 'staff',
                'staff': staff,
            },
        )


class StaffDetailView(TemplateResponseMixin, View):
    template_name = 'staff/detail.html'

    def get(self, request: HttpRequest, stage: str, slug: str):
        return self.render_to_response(
            context={
                'active_page': 'staff',
                'staff': get_staff_by_slug(slug=slug),
            },
        )
