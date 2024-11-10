from django.http import HttpRequest
from django.views.generic import View, TemplateView
from django.views.generic.base import TemplateResponseMixin

from staff.services import get_staff
from works.services import get_works
from services.services import get_service_groups


class MainView(TemplateResponseMixin, View):
    template_name = 'main/main.html'

    def get(self, request: HttpRequest):
        staff = get_staff()
        works = get_works()
        service_groups = get_service_groups()
        if len(staff) > 4:
            staff = staff[:4]
        if len(works) > 3:
            works = works[:3]
        if len(service_groups) > 6:
            service_groups = service_groups[:6]
        return self.render_to_response(
            context={
                'active_page': '',
                'works': works,
                'staff': staff,
                'service_groups': service_groups,
            },
        )


class SitemapView(TemplateView):
    """Просмотр для отображения карты сайта."""

    template_name = 'main/site_map.html'


class BadRequestView(TemplateView):
    template_name = 'errors/400.html'
    status_code = 400


class PermissionDeniedView(TemplateView):
    template_name = 'errors/403.html'
    status_code = 403


class PageNotFoundView(TemplateView):
    template_name = 'errors/404.html'
    status_code = 404


class ServerErrorView(TemplateView):
    template_name = 'errors/500.html'
    status_code = 500
