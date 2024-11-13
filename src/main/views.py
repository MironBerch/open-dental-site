from django.http import HttpRequest
from django.views.generic import View, TemplateView
from django.views.generic.base import TemplateResponseMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse

from main.forms import SearchForm
from staff.services import get_staff
from works.services import get_works
from services.services import get_service_groups
from main.services import get_search_results


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
            print(results)
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
