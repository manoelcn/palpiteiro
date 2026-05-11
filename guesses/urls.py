from django.urls import path
from guesses.views import GuessCreateView, GuessUpdateView


urlpatterns = [
    path('guesses/<int:group_pk>/<int:match_pk>/create/', GuessCreateView.as_view(), name='guess-create'),
    path('guesses/<int:group_pk>/<int:pk>/update/', GuessUpdateView.as_view(), name='guess-update'),
]
