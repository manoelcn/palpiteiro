from django.urls import path
from core.views import CoreView, DashboardView


urlpatterns = [
    path('', CoreView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
