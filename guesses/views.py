from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from guesses.models import Guess
from guesses.forms import GuessForm


class GuessCreateView(LoginRequiredMixin, CreateView):
    model = Guess
    template_name = 'guess_create.html'
    form_class = GuessForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.group_id = self.kwargs['group_pk']
        form.instance.match_id = self.kwargs['match_pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('group-detail', kwargs={'pk': self.kwargs['group_pk']})
