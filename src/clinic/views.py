from django.http import HttpRequest
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from clinic.services import get_clinic_requisites, get_clinic_about, get_clinic_licenses

#  from django.core.paginator import Paginator


class RequisitesView(TemplateResponseMixin, View):
    template_name = 'clinic/requisites.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'clinic',
                'requisites': get_clinic_requisites(),
            },
        )


class AboutView(TemplateResponseMixin, View):
    template_name = 'clinic/about.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'clinic',
                'company': get_clinic_about(),
            },
        )


class LicensesView(TemplateResponseMixin, View):
    template_name = 'clinic/licenses.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'clinic',
                'licenses': get_clinic_licenses(),
            },
        )
