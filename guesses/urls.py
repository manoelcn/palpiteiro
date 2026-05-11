from django.urls import path
from guesses.views import GuessCreateView


urlpatterns = [
    path('guesses/<int:group_pk>/<int:match_pk>/create/', GuessCreateView.as_view(), name='guess-create'),
]
