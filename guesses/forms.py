from django import forms
from guesses.models import Guess


class GuessForm(forms.ModelForm):
    class Meta:
        model = Guess
        fields = ['home_score', 'away_score']
