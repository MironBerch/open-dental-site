from debug_toolbar.toolbar import debug_toolbar_urls

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic.base import TemplateView

from clinic.views import (
    AboutView,
    ContactsView,
    LicensesView,
    PolicyView,
    PricesView,
    ReviewsView,
    ServicesGroupsView,
    ServicesGroupView,
    ServiceView,
    StaffView,
    WorksView,
    WorkView,
)
from config.sitemap import (
    MainStaticViewSitemap,
    ServiceGroupSitemap,
    ServiceSitemap,
    StaticViewSitemap,
    WorkSitemap,
)
from main.views import MainView, SearchAPIView, SearchView, SitemapView

sitemaps = {
    'static': StaticViewSitemap,
    'service_groups': ServiceGroupSitemap,
    'services': ServiceSitemap,
    'works': WorkSitemap,
    'main_static': MainStaticViewSitemap,
}

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
        name='staff',
    ),
    path(
        route='policy/',
        view=PolicyView.as_view(),
        name='policy',
    ),
    # SEO
    path(
        'sitemap.xml',
        sitemap,
        {
            'sitemaps': sitemaps,
        },
        name='django.contrib.sitemaps.views.sitemap',
    ),
    path(
        'robots.txt',
        TemplateView.as_view(
            template_name='robots.txt',
            content_type='text/plain',
        ),
    ),
    # ckeditor5
    path('ckeditor5/', include('django_ckeditor_5.urls')),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
