from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.db import IntegrityError
from django.contrib import messages
from guesses.models import Guess
from guesses.forms import GuessForm
from matches.models import Match


class GuessCreateView(LoginRequiredMixin, CreateView):
    model = Guess
    template_name = 'guess_create.html'
    form_class = GuessForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.group_id = self.kwargs['group_pk']
        form.instance.match_id = self.kwargs['match_pk']
        try:
            response = super().form_valid(form)
            messages.success(self.request, 'Palpite salvo com sucesso!')
            return response
        except IntegrityError:
            messages.error(self.request, 'Você já fez um palpite para esse jogo!')
            return self.form_invalid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['match'] = Match.objects.get(pk=self.kwargs['match_pk'])
        return kwargs

    def get_success_url(self):
        return reverse_lazy('group-detail', kwargs={'pk': self.kwargs['group_pk']})


class GuessUpdateView(LoginRequiredMixin, UpdateView):
    model = Guess
    template_name = 'guess_update.html'
    form_class = GuessForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['match'] = self.get_object().match
        return kwargs
    
    def get_queryset(self):
        return Guess.objects.filter(user=self.request.user, match__status='TIMED')
    
    def get_success_url(self):
        return reverse_lazy('group-detail', kwargs={'pk': self.kwargs['group_pk']})
    
    def form_valid(self, form):
        messages.success(self.request, 'Palpite atualizado com sucesso!')
        return super().form_valid(form)
