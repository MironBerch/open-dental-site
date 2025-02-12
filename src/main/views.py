from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, View
from django.views.generic.base import TemplateResponseMixin

from clinic.services import get_clinic_licenses, get_published_reviews, get_staff
from main.forms import SearchForm
from main.services import get_search_results
from services.models import Service, ServiceGroup
from services.services import get_service_groups
from works.services import get_works


class MainView(TemplateResponseMixin, View):
    template_name = 'main/main.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': '',
                'works': get_works(),
                'staff': get_staff(),
                'service_groups': get_service_groups(),
                'reviews': get_published_reviews().order_by('-created_at'),
                'licenses': get_clinic_licenses(),
            },
        )


class SearchAPIView(TemplateResponseMixin, View):
    def get(self, request):
        query = request.GET.get('query', '')
        results = []
        if query:
            results = get_search_results(query)
        return JsonResponse(results, safe=False)


class SearchView(TemplateResponseMixin, View):
    template_name = 'main/search.html'
    form_class = SearchForm

    def get(self, request: HttpRequest):
        query = request.GET.get('query', '')
        results = []
        if query:
            results = get_search_results(query)
        return self.render_to_response(
            context={
                'form': self.form_class(initial={'query': query}),
                'results': results,
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            return redirect(f'{reverse('search_view')}?query={query}')
        return self.render_to_response(
            context={
                'form': form,
            },
        )


class SitemapView(TemplateView):
    """Просмотр для отображения карты сайта."""
    template_name = 'main/site_map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_groups = ServiceGroup.objects.all()
        filtered_service_groups = []
        for service_group in service_groups:
            services_by_group = Service.objects.filter(group=service_group, published=True)
            filtered_service_groups.append(service_group) if services_by_group else None
        context['service_groups'] = filtered_service_groups
        return context


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
