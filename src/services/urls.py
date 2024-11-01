from django.urls import path

from services.views import ServicesGroupsView, ServicesGroupView, ServiceView

urlpatterns = [
    path(
        route='services/',
        view=ServicesGroupsView.as_view(),
        name='services_groups',
    ),
    path(
        route='services/<slug>/',
        view=ServicesGroupView.as_view(),
        name='services_group',
    ),
    path(
        route='service/<slug>/',
        view=ServiceView.as_view(),
        name='service',
    ),
]
