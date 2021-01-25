# Generated by Django 3.1.4 on 2021-01-05 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(max_length=20)),
                ('game_type', models.CharField(choices=[('FR', 'Friend'), ('CO', 'Computer')], default='FR', max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('player_joined', models.BooleanField(default=True)),
                ('game_start', models.TimeField(default=datetime.datetime(2021, 1, 5, 13, 12, 14, 256269))),
                ('last_modified', models.TimeField(auto_now=True)),
                ('player_1_input', models.CharField(choices=[('RO', 'ROCK'), ('PA', 'PAPER'), ('SC', 'SCISSORS'), ('SP', 'SPOCK'), ('LI', 'LIZARD')], default=None, max_length=2)),
                ('player_2_input', models.CharField(choices=[('RO', 'ROCK'), ('PA', 'PAPER'), ('SC', 'SCISSORS'), ('SP', 'SPOCK'), ('LI', 'LIZARD')], default=None, max_length=2)),
            ],
        ),
    ]
