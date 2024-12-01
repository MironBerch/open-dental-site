from debug_toolbar.toolbar import debug_toolbar_urls

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from clinic.views import (
    AboutView,
    ContactsView,
    LicensesView,
    LicenseView,
    PolicyView,
    RequisitesView,
)
from main.views import MainView, SearchAPIView, SearchView, SitemapView
from prices.views import PricesView
from reviews.views import ReviewsView
from services.views import ServicesGroupsView, ServicesGroupView, ServiceView
from staff.views import StaffByStageView, StaffDetailView, StaffView
from works.views import WorksView, WorkView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Gallery
    path('gallery/', WorksView.as_view(), name='gallery'),
    path('gallery/<slug>/', WorkView.as_view(), name='work'),

    # Services
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
    path(
        route='price/',
        view=PricesView.as_view(),
        name='prices',
    ),

    path(
        route='sitemap/',
        view=SitemapView.as_view(),
        name='site_map',
    ),
    path(
        route='',
        view=MainView.as_view(),
        name='main',
    ),

    # Search
    path(
        route='api/search/',
        view=SearchAPIView.as_view(),
        name='search',
    ),
    path(
        route='search/',
        view=SearchView.as_view(),
        name='search_view',
    ),

    # Company
    path(
        route='company/requisites/',
        view=RequisitesView.as_view(),
        name='requisites',
    ),
    path(
        route='company/',
        view=AboutView.as_view(),
        name='company',
    ),
    path(
        route='company/licenses/',
        view=LicensesView.as_view(),
        name='licenses',
    ),
    path(
        route='company/licenses/<slug>/',
        view=LicenseView.as_view(),
        name='license',
    ),
    path(
        route='company/contacts/',
        view=ContactsView.as_view(),
        name='contacts',
    ),
    path(
        route='company/reviews/',
        view=ReviewsView.as_view(),
        name='reviews',
    ),
    path(
        route='company/staff/',
        view=StaffView.as_view(),
        name='staff_list',
    ),
    path(
        route='company/staff/<stage>/',
        view=StaffByStageView.as_view(),
        name='staff_by_stage',
    ),
    path(
        route='company/staff/<stage>/<slug>/',
        view=StaffDetailView.as_view(),
        name='staff',
    ),

    path(
        route='policy/',
        view=PolicyView.as_view(),
        name='policy',
    ),

    path('ckeditor5/', include('django_ckeditor_5.urls')),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
