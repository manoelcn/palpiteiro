from django import forms
from django.db.models import Q
from groups.models import Group
from matches.models import Match


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'matches']
        labels = {
            'name': 'Nome do bolão',
            'matches': 'Partidas',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Bolão da Família',
            }),
            'matches': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'size': '8',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'matches' in self.fields:
            if not self.instance.pk:
                self.fields['matches'].queryset = Match.objects.filter(status='TIMED')
            else:
                self.fields['matches'].queryset = Match.objects.filter(
                    Q(status='TIMED') | Q(id__in=self.instance.matches.all())
                ).distinct()


class InviteCodeForm(forms.Form):
    invite_code = forms.CharField(
        max_length=5,
        label='Código do bolão',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: abc12',
        })
    )
