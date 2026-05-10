from django.urls import path
from groups.views import GroupCreateView, GroupListView, GroupJoinView


urlpatterns = [
    path('groups/create/', GroupCreateView.as_view(), name='group-create'),
    path('groups/list/', GroupListView.as_view(), name='group-list'),
    path('groups/join/', GroupJoinView.as_view(), name='group-join'),
]
