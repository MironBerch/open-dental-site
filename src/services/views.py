from django.http import HttpRequest
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from services.services import get_service_groups


class ServicesView(TemplateResponseMixin, View):
    template_name = 'services/groups.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'services',
                'services': get_service_groups(),
            },
        )
