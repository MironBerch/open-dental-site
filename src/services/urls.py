from django.urls import path

from services.views import ServicesView

urlpatterns = [
    path(
        route='services/',
        view=ServicesView.as_view(),
        name='services',
    ),
]
