from django.http import HttpRequest
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from services.services import (get_group_by_slug, get_service_by_slug,
                               get_service_groups, get_services_by_group)


class ServicesGroupsView(TemplateResponseMixin, View):
    template_name = 'services/groups.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'services',
                'services': get_service_groups(),
            },
        )


class ServicesGroupView(TemplateResponseMixin, View):
    template_name = 'services/group.html'

    def get(self, request: HttpRequest, slug: str):
        group = get_group_by_slug(slug)
        return self.render_to_response(
            context={
                'active_page': 'services',
                'group': group,
                'services': get_services_by_group(group),
            },
        )


class ServiceView(TemplateResponseMixin, View):
    template_name = 'services/service.html'

    def get(self, request: HttpRequest, slug: str):
        print(get_service_by_slug(slug))
        service, prices = get_service_by_slug(slug)
        return self.render_to_response(
            context={
                'active_page': 'services',
                'service': service,
                'prices': prices,
            },
        )
