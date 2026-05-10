from django import forms
from groups.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class InviteCodeForm(forms.Form):
    invite_code = forms.CharField(max_length=5)
