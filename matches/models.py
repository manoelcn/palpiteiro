from django.db import models


STATUS_CHOICE = [
    ('scheduled', 'scheduled'),
    ('in_progress', 'in_progress'),
    ('finished', 'finished'),
]

class Match(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    kickoff = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICE, default='scheduled')
    home_score = models.IntegerField(null=True)
    away_score = models.IntegerField(null=True)
    api_match_id = models.CharField(max_length=100)
