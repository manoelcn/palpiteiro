from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView
from accounts.forms import AccountForm
from accounts.models import CustomUser


class AccountRegister(CreateView):
    model = CustomUser
    template_name = 'account_create.html'
    form_class = AccountForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
