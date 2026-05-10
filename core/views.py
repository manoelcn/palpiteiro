from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class CoreView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
