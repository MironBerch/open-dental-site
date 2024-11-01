from django.urls import path

from .views import StaffView

urlpatterns = [
    path('staff/', StaffView.as_view(), name='staff'),
]
