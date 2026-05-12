from django import forms
from guesses.models import Guess


class GuessForm(forms.ModelForm):
    class Meta:
        model = Guess
        fields = ['home_score', 'away_score']
        widgets = {
            'home_score': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'away_score': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        match = kwargs.pop('match', None)
        super().__init__(*args, **kwargs)
        if match:
            self.fields['home_score'].label = match.home_team
            self.fields['away_score'].label = match.away_team
