from django.http import HttpRequest
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from works.services import get_work_by_slug, get_work_images_by_work_slug, get_works


class WorksView(TemplateResponseMixin, View):
    template_name = 'works/list.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'works',
                'works': get_works(),
            },
        )


class WorkView(TemplateResponseMixin, View):
    template_name = 'works/detail.html'

    def get(self, request: HttpRequest, slug: str):
        return self.render_to_response(
            context={
                'active_page': 'works',
                'work': get_work_by_slug(slug=slug),
                'images': get_work_images_by_work_slug(slug=slug),
            },
        )
