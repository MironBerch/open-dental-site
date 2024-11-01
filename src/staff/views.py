from django.http import HttpRequest
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from staff.services import get_all_staff


class StaffView(TemplateResponseMixin, View):
    template_name = 'staff/view.html'

    def get(self, request: HttpRequest):
        staff = get_all_staff()
        return self.render_to_response(
            context={
                'active_page': 'staff',
                'managers':  staff['Руководитель'],
                'administrators': staff['Администратор'],
                'medics': staff['Мед персонал'],
                'junior_medics': staff['Младщий мед персонал'],
            },
        )
