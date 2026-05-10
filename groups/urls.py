from django.urls import path
from groups.views import GroupCreateView, GroupListView


urlpatterns = [
    path('groups/create/', GroupCreateView.as_view(), name='group-create'),
    path('groups/list/', GroupListView.as_view(), name='group-list'),
]
