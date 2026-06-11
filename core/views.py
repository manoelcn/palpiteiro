from django.shortcuts import render
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from accounts.models import CustomUser
from groups.models import Group
from guesses.models import Guess
from matches.models import Match


class CoreView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class DashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_users_active'] = CustomUser.objects.filter(is_active=True).count()
        context['total_groups'] = Group.objects.count()
        context['total_guesses'] = Guess.objects.count()
        context['matches_finished'] = Match.objects.filter(status='FINISHED').count()
        context['groups'] = Group.objects.select_related('owner').annotate(
            total_members=Count('memberships')
        ).order_by('-total_members')
        
        return context
