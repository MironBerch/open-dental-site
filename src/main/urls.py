from django.urls import path

from main.views import SitemapView, MainView, SearchAPIView, SearchView

urlpatterns = [
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
]
