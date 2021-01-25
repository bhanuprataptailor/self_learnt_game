# Generated by Django 3.1.4 on 2021-01-05 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20210105_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_start',
            field=models.TimeField(default=datetime.datetime(2021, 1, 5, 18, 11, 35, 727801)),
        ),
        migrations.AlterField(
            model_name='players',
            name='player_choice',
            field=models.CharField(blank=True, choices=[('RO', 'ROCK'), ('PA', 'PAPER'), ('SC', 'SCISSORS'), ('SP', 'SPOCK'), ('LI', 'LIZARD')], default=None, max_length=2, null=True),
        ),
    ]