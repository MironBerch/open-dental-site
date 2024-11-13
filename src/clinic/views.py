from django.http import HttpRequest
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from clinic.services import (
    get_clinic_about,
    get_clinic_licenses,
    get_clinic_requisites,
    get_clinic_contacts,
    get_clinic_license_by_slug,
)

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


class LicenseView(TemplateResponseMixin, View):
    template_name = 'clinic/license.html'

    def get(self, request: HttpRequest, slug: str):
        return self.render_to_response(
            context={
                'active_page': 'clinic',
                'license': get_clinic_license_by_slug(slug),
            },
        )


class ContactsView(TemplateResponseMixin, View):
    template_name = 'clinic/contacts.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'contacts',
                'contacts': get_clinic_contacts(),
            },
        )
