from django.utils.deprecation import MiddlewareMixin

from clinic.services import get_clinic_contact, get_clinic_media


class BaseContextMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        if hasattr(response, 'context_data'):
            response.context_data.update(
                {
                    'media': get_clinic_media(),
                    'contact': get_clinic_contact(),
                }
            )
        return response
