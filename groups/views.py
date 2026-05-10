from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.edit import FormView
from groups.models import Group, Membership
from groups.forms import GroupForm, InviteCodeForm

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'group_create.html'
    form_class = GroupForm
    success_url = reverse_lazy('group-list')

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
        return Group.objects.filter(memberships__user=self.request.user)


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


class GroupLeaveView(LoginRequiredMixin, DeleteView):
    model = Membership
    template_name = 'group_delete.html'
    success_url = reverse_lazy('group-list')

    def get_queryset(self):
        return Membership.objects.filter(user=self.request.user)
