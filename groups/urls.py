from django.urls import path
from groups.views import GroupCreateView, GroupListView, GroupJoinView, GroupLeaveView, GroupDetailView, GroupUpdateView, GroupDeleteView, GroupRankingView


urlpatterns = [
    path('groups/create/', GroupCreateView.as_view(), name='group-create'),
    path('groups/<int:pk>/update/', GroupUpdateView.as_view(), name='group-update'),
    path('groups/list/', GroupListView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('groups/join/', GroupJoinView.as_view(), name='group-join'),
    path('groups/leave/<int:pk>/', GroupLeaveView.as_view(), name='group-leave'),
    path('groups/<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),
    path('groups/<int:pk>/ranking/', GroupRankingView.as_view(), name='group-ranking'),
]
