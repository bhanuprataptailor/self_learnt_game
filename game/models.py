from django.db import models
from datetime import datetime
# Create your models here.


class Players(models.Model):
    ROCK = 'RO'
    PAPER = 'PA'
    SCISSORS = 'SC'
    SPOCK = 'SP'
    LIZARD = 'LI'
    player_id = models.CharField(max_length=512)
    player_name = models.CharField(max_length=512)
    PLAYER_CHOICES = [
        (ROCK, 'ROCK'),
        (PAPER, 'PAPER'),
        (SCISSORS, 'SCISSORS'),
        (SPOCK, 'SPOCK'),
        (LIZARD, 'LIZARD')
    ]
    player_choice = models.CharField(
        max_length=2,
        choices=PLAYER_CHOICES,
        default=None,
        null=True,
        blank=True
    )


class Game(models.Model):
    FRIEND = 'FR'
    COMPUTER = 'CO'
    GAME_TYPE_CHOICES = [
        (FRIEND, 'Friend'),
        (COMPUTER, 'Computer'),
    ]

    game_id = models.CharField(max_length=20)
    game_type = models.CharField(
        max_length=2,
        choices=GAME_TYPE_CHOICES,
        default=FRIEND
    )
    is_active = models.BooleanField(default=True)
    player_joined = models.BooleanField(default=None)
    game_start = models.TimeField(default=datetime.now())
    last_modified = models.TimeField(auto_now=True)
    player_1 = models.ForeignKey(Players, on_delete=models.CASCADE, related_name='player1_game', null=True, blank=True)
    player_2 = models.ForeignKey(Players, on_delete=models.CASCADE, related_name='player2_game', null=True, blank=True)
    winner = models.ForeignKey(Players, on_delete=models.CASCADE, related_name='winner_game', null=True, blank=True)

