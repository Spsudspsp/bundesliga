from datetime import datetime
from django import views
import requests
from django.shortcuts import render


class HomeView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class GamesView(views.View):
    def get(self, request, *args, **kwargs):
        res = requests.get('https://www.openligadb.de/api/getmatchdata/bl1')
        data = res.json()

        games_sorted = sorted(data, key=lambda x: datetime.strptime(x['MatchDateTime'][:10], '%Y-%m-%d'))
        next_game_date = games_sorted[0]['MatchDateTime'][:10]

        data = [i for i in data if i['MatchDateTime'][:10] == next_game_date]

        for match in data:
            match['date'], match['time'] = match['MatchDateTime'].split('T')
        context = {
            'data': data
        }
        return render(request, 'next_game.html', context)


class TeamsDetailsView(views.View):
    def get(self, request, *args, **kwargs):
        res = requests.get(f'https://www.openligadb.de/api/getbltable/bl1/{datetime.now().year}')
        data = res.json()

        for team in data:
            team['win_loss_ratio'] = team['Won'] + team['Lost'] / team['Matches']

        context = {
            'data': data
        }
        return render(request, 'team_details.html', context)


class AllGamesView(views.View):
    def get(self, request, *args, **kwargs):
        res = requests.get('https://www.openligadb.de/api/getmatchdata/bl1')
        data = res.json()

        for match in data:
            match['date'], match['time'] = match['MatchDateTime'].split('T')

        context = {
            'data': data
        }
        return render(request, 'all_games.html', context)