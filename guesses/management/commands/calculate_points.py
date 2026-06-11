from django.core.management.base import BaseCommand
from guesses.models import Guess
from matches.models import Match


class Command(BaseCommand):
    help = 'Calcula pontos dos palpites'

    def handle(self, *args, **kwargs):
        Guess.objects.exclude(match__status='FINISHED').update(points=None)
        matches_finished = Match.objects.filter(status='FINISHED')
        count = 0
        for match in matches_finished:
            guesses = Guess.objects.filter(match=match)

            if match.home_score > match.away_score:
                real_result = 'home'
            elif match.away_score > match.home_score:
                real_result = 'away'
            else:
                real_result = 'draw'

            for guess in guesses:
                if guess.home_score == match.home_score and guess.away_score == match.away_score:
                    points = 3
                elif guess.home_score > guess.away_score and real_result == 'home':
                    points = 1
                elif guess.away_score > guess.home_score and real_result == 'away':
                    points = 1
                elif guess.home_score == guess.away_score and real_result == 'draw':
                    points = 1
                else:
                    points = 0

                guess.points = points
                guess.save()
                count += 1

        self.stdout.write(f'{count} palpites calculados com sucesso!')
