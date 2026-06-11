from django.shortcuts import render
from django.db import IntegrityError
from django.db.models import Sum, Q
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.views.generic.edit import FormView
from django.contrib import messages
from groups.models import Group, Membership
from groups.forms import GroupForm, InviteCodeForm
from matches.models import Match
from guesses.models import Guess

class GroupCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Group
    template_name = 'group_create.html'
    form_class = GroupForm
    success_url = reverse_lazy('group-list')
    permission_required = 'groups.add_group'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        Membership.objects.create(user=self.request.user, group=self.object)
        return response


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'group_list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        groups = Group.objects.filter(memberships__user=self.request.user)
        for group in groups:
            group.my_membership = group.memberships.filter(user=self.request.user).first()
        return groups


class GroupJoinView(LoginRequiredMixin, FormView):
    template_name = 'group_join.html'
    form_class = InviteCodeForm
    success_url = reverse_lazy('group-list')

    def form_valid(self, form):
        try:
            group = Group.objects.get(invite_code=form.cleaned_data['invite_code'])
            Membership.objects.create(user=self.request.user, group=group)
            return super().form_valid(form)
        except Group.DoesNotExist:
            form.add_error('invite_code', 'Código inválido.')
            return self.form_invalid(form)
        except IntegrityError:
            messages.error(self.request, 'Você já faz parte desse bolão.')
            return self.form_invalid(form)


class GroupLeaveView(LoginRequiredMixin, DeleteView):
    model = Membership
    template_name = 'group_leave.html'
    success_url = reverse_lazy('group-list')

    def get_queryset(self):
        return Membership.objects.filter(user=self.request.user).exclude(group__owner=self.request.user)


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'group_detail.html'
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group_matches = self.object.matches.all().order_by('kickoff')
        
        context['matches'] = group_matches.filter(status='TIMED')
        
        guesses = Guess.objects.filter(user=self.request.user, group=self.object, match__in=group_matches)
        context['guesses'] = guesses
        context['guessed_match_ids'] = list(guesses.values_list('match_id', flat=True))
        
        past_matches = group_matches.exclude(status='TIMED').order_by('-kickoff')
        
        guesses_dict = {guess.match_id: guess for guess in guesses}
        for match in past_matches:
            match.user_guess = guesses_dict.get(match.id)
            
        context['past_matches'] = past_matches
        return context


class GroupUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Group
    template_name = 'group_update.html'
    form_class = GroupForm
    success_url = reverse_lazy('group-list')
    permission_required = 'groups.change_group'

    def get_queryset(self):
        return Group.objects.filter(owner=self.request.user)


class GroupDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Group
    template_name = 'group_delete.html'
    success_url = reverse_lazy('group-list')
    permission_required = 'groups.delete_group'

    def get_queryset(self):
        return Group.objects.filter(owner=self.request.user)


class GroupRankingView(LoginRequiredMixin, ListView):
    model = Membership
    template_name = 'group_ranking.html'
    context_object_name = 'ranking'

    def get_queryset(self):
        group_id = self.kwargs.get('pk')
        queryset = Membership.objects.filter(
            group_id=group_id
        ).exclude(
            user__is_staff=True
        ).exclude(
            user__is_superuser=True
        ).annotate(
            total_points=Coalesce(
                Sum(
                    'user__guesses__points', 
                    filter=Q(user__guesses__group_id=group_id)
                ), 
                0
            )
        ).order_by('-total_points')
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = get_object_or_404(Group, pk=self.kwargs.get('pk'))
        return context
