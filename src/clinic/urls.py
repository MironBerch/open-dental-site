from django.urls import path

from clinic.views import RequisitesView

urlpatterns = [
    path(
        route='requisites/',
        view=RequisitesView.as_view(),
        name='requisites',
    ),
]
