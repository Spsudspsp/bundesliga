from django.contrib.auth.decorators import login_required
from django.urls import path
from games.views import GamesView, TeamsDetailsView, AllGamesView, HomeView

urlpatterns = [
    path('next_gameday/', login_required(GamesView.as_view()), name='games'),
    path('teams/', login_required(TeamsDetailsView.as_view()), name='teams'),
    path('all_games/', login_required(AllGamesView.as_view()), name='all_games'),
    path('', HomeView.as_view(), name='home'),
]
