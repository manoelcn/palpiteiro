from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import AccountForm
from accounts.models import CustomUser


class AccountRegister(CreateView):
    model = CustomUser
    template_name = 'account_create.html'
    form_class = AccountForm
    success_url = reverse_lazy('login')
