from django.shortcuts import render
from django.http import HttpResponse
from game.models import Game, Players
from game.serializers import GameSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from uuid import uuid4
from datetime import datetime


def index(request):
    return HttpResponse("Rock Paper Scissors")
# Create your views here.


@api_view(('GET', 'POST'))
def create_game(request):
    if request.method == 'GET':
        print(request.GET["q"])
        game = Game.objects.all()
        print(game)
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        game_id = request.data.get('game_id')
        player_id = request.data.get('player_name')
        player_name = request.data.get('player_name')
        player_queryset = Players.objects.get_or_create(
            player_id=player_id,
            player_name=player_name
        )
        # player_queryset.save()
        game_queryset = Game.objects.get_or_create(
            game_id=game_id,
            is_active=True,
            player_1=player_queryset,
            game_type='FR',
            player_joined=False
        )
        # game_queryset.save()
        serializer = GameSerializer(game_queryset, many=True)
        return Response(serializer.data)


@api_view(('GET', 'POST'))
def join_game(request):
    if request.method == 'POST':
        game_id = request.data.get('game_id')
        player_id = request.data.get('player_name')
        player_name = request.data.get('player_name')
        try:
            game_queryset = Game.objects.get(
                game_id=game_id,
                is_active=True,
                game_type='FR',
                player_joined=False
            )
            player_queryset = Players.objects.get_or_create(
                player_id=player_id,
                player_name=player_name
            )
            print(player_queryset)
            game_queryset.player_2 = player_queryset
            game_queryset.player_joined = True
            serializer = GameSerializer(game_queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            print(str(e))
