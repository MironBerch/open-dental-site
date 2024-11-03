from django.http import HttpRequest
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from prices.models import PriceGroup


class PricesView(TemplateResponseMixin, View):
    template_name = 'prices/list.html'

    def get(self, request: HttpRequest):
        return self.render_to_response(
            context={
                'active_page': 'prices',
                'price_groups': PriceGroup.objects.prefetch_related('price_set').all()
            },
        )
