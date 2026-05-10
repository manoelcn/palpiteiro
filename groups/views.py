from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from groups.models import Group
from groups.forms import GroupForm

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'group_create.html'
    form_class = GroupForm
    success_url = reverse_lazy('group-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
