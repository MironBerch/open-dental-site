from os import environ

from django.utils.deprecation import MiddlewareMixin
from django.utils.safestring import mark_safe

from clinic.services import get_clinic_contact


class BaseContextMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        if hasattr(response, 'context_data'):
            response.context_data.update(
                {
                    'contact': get_clinic_contact(),
                    'yandex_metrika': mark_safe(environ.get('YANDEX_METRIKA', '')),
                }
            )
        return response
