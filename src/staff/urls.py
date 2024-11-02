from django.urls import path

from staff.views import StaffView, StaffDetailView

urlpatterns = [
    path('staff/', StaffView.as_view(), name='staff_list'),
    path('staff/<slug>/', StaffDetailView.as_view(), name='staff'),
]
