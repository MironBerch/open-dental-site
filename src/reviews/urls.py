from django.urls import path

from reviews.views import ReviewsView

urlpatterns = [
    path(
        route='',
        view=ReviewsView.as_view(),
        name='reviews',
    ),
]
