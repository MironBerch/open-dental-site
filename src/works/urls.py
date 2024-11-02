from django.urls import path

from works.views import WorksView, WorkView

urlpatterns = [
    path('gallery/', WorksView.as_view(), name='gallery'),
    path('gallery/<slug>/', WorkView.as_view(), name='work'),
]
