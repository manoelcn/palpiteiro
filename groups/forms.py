from django import forms
from groups.models import Group


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


class InviteCodeForm(forms.Form):
    invite_code = forms.CharField(max_length=5)
