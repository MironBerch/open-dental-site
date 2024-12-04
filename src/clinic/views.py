from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from clinic.forms import ReviewForm
from clinic.services import (
    get_clinic_about,
    get_clinic_contacts,
    get_clinic_license_by_slug,
    get_clinic_licenses,
    get_clinic_policy,
    get_clinic_requisites,
    get_published_reviews,
)


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


class PolicyView(TemplateResponseMixin, View):
    template_name = 'clinic/policy.html'

    def get(self, request: HttpRequest, slug: str):
        return self.render_to_response(
            context={
                'active_page': 'clinic',
                'policy': get_clinic_policy(),
            },
        )


class ReviewsView(TemplateResponseMixin, View):
    template_name = 'clinic/reviews.html'
    form_class = ReviewForm

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response(
            context={
                'form': self.form_class(),
                'active_page': 'reviews',
                'reviews': get_published_reviews().order_by('-id'),
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.add_message(
                request,
                messages.SUCCESS,
                'Отзыв успешно оставлен',
            )
            form.save()
            return redirect('reviews')
        return self.render_to_response(
            context={
                'form': self.form_class,
                'active_page': 'reviews',
                'reviews': get_published_reviews().order_by('-id'),
            },
        )
