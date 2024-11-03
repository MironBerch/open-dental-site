from django.urls import path

from prices.views import PricesView

urlpatterns = [
    path(
        route='price/',
        view=PricesView.as_view(),
        name='prices',
    ),
]
