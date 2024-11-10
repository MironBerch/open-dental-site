from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('clinic.urls')),
    path('', include('services.urls')),
    path('', include('staff.urls')),
    path('', include('works.urls')),
    path('', include('prices.urls')),
    path('reviews/', include('reviews.urls')),

    path('ckeditor5/', include('django_ckeditor_5.urls')),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
