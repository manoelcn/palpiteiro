from django.core.management.base import BaseCommand
import requests
import json
from app.settings import FOOTBALL_API_KEY
from matches.models import Match

class Command(BaseCommand):
    help = 'Sincroniza os jogos da Copa do Mundo com a API'

    def handle(self, *args, **kwargs):
        url = 'https://api.football-data.org/v4/competitions/WC/matches'
        headers = { 'X-Auth-Token': FOOTBALL_API_KEY }
        response = requests.get(url, headers=headers)
        if response:
            count = 0
            for match in response.json()['matches']:   
                if match['homeTeam']['name'] is None or match['awayTeam']['name'] is None:
                    continue
                Match.objects.update_or_create(
                    api_match_id=match['id'],
                    defaults={
                        'home_team': match['homeTeam']['name'],
                        'away_team': match['awayTeam']['name'],
                        'kickoff': match['utcDate'],
                        'status': match['status'],
                        'home_score': match['score']['fullTime']['home'],
                        'away_score': match['score']['fullTime']['away'],
                    }
                )
                count += 1
        self.stdout.write(f'{count} jogos sincronizados com sucesso!')
