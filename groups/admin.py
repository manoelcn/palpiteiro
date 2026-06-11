from django.contrib import admin
from .models import Group, Membership

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'invite_code', 'owner', 'created_at')
    search_fields = ('name', 'invite_code', 'owner__username')
    readonly_fields = ('invite_code',)

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'joined_at')
    search_fields = ('user__username', 'group__name')
    list_filter = ('group',)
