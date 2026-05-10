from django.urls import path
from groups.views import GroupCreateView


urlpatterns = [
    path('groups/create/', GroupCreateView.as_view(), name='group-create'),
]
