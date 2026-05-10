from django.db import models
from accounts.models import CustomUser
from groups.models import Group
from matches.models import Match


class Guess(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='guesses')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='guesses')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='guesses')
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    points = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'group', 'match')
