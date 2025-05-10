from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from clinic.forms import ReviewForm
from clinic.models import PriceGroup
from clinic.services import (
    get_all_staff,
    get_clinic_about,
    get_clinic_contacts,
    get_clinic_licenses,
    get_clinic_policy,
    get_group_by_slug,
    get_published_reviews,
    get_service_by_slug,
    get_service_groups,
    get_services_by_group,
    get_services_by_groups,
    get_work_by_slug,
    get_work_images_by_work_slug,
    get_works,
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

    def get(self, request: HttpRequest):
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
                'reviews': get_published_reviews().order_by('-created_at'),
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


class StaffView(TemplateResponseMixin, View):
    template_name = 'clinic/staff.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'staff',
                'staff': get_all_staff(),
            },
        )


class PricesView(TemplateResponseMixin, View):
    template_name = 'clinic/prices.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'prices',
                'price_groups': PriceGroup.objects.prefetch_related('price_set').all(),
            },
        )


class ServicesGroupsView(TemplateResponseMixin, View):
    template_name = 'clinic/services_groups.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'services',
                'services': get_service_groups(),
            },
        )


class ServicesGroupView(TemplateResponseMixin, View):
    template_name = 'clinic/services_group.html'

    def get(self, request: HttpRequest, slug: str):
        group = get_group_by_slug(slug)
        services_by_group = get_services_by_groups()
        return self.render_to_response(
            context={
                'active_page': 'services',
                'group': group,
                'services': get_services_by_group(group),
                'service_groups': services_by_group,
            },
        )


class ServiceView(TemplateResponseMixin, View):
    template_name = 'clinic/service.html'

    def get(self, request: HttpRequest, slug: str):
        service, prices = get_service_by_slug(slug)
        return self.render_to_response(
            context={
                'active_page': 'services',
                'service': service,
                'prices': prices,
            },
        )


class WorksView(TemplateResponseMixin, View):
    template_name = 'clinic/works.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'works',
                'works': get_works(),
            },
        )


class WorkView(TemplateResponseMixin, View):
    template_name = 'clinic/work.html'

    def get(self, request: HttpRequest, slug: str):
        return self.render_to_response(
            context={
                'active_page': 'works',
                'work': get_work_by_slug(slug=slug),
                'images': get_work_images_by_work_slug(slug=slug),
            },
        )
