from django.urls import path

from clinic.views import AboutView, LicensesView, RequisitesView, ContactsView, LicenseView

urlpatterns = [
    path(
        route='requisites/',
        view=RequisitesView.as_view(),
        name='requisites',
    ),
    path(
        route='company/',
        view=AboutView.as_view(),
        name='company',
    ),
    path(
        route='licenses/',
        view=LicensesView.as_view(),
        name='licenses',
    ),
    path(
        route='licenses/<slug>/',
        view=LicenseView.as_view(),
        name='license',
    ),
    path(
        route='contacts/',
        view=ContactsView.as_view(),
        name='contacts',
    ),
]
