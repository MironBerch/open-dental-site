from django.urls import path

from main.views import SitemapView, MainView, SearchView

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
        route='search/',
        view=SearchView.as_view(),
        name='search',
    ),
]
