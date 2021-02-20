"""
File for different tests on the features of the class Tournament
"""

from models.tournament import Tournament
from models.players import Player
from models.serializable import Serializable


# Sample Values

player1 = Player('aKONdé', 'Axel', '1986-05-02', Player.Gender.MALE, 1)
player2 = Player('Berd', 'Bernard', '1982-03-01', 'FEMALE', 3)
player3 = Player('CERAS', 'Cédric', '1978-04-26', 'FEMALE', 2)
player4 = Player('Deflar', 'Didier', '1991-12-21', 'FEMALE', 4)


name = 'Best Tournament Ever'
location = 'Geneve'
date = '1987-02-28'
rounds_count = 0
rounds = 3
players = [player1, player2, player3, player4]
time_control = 'BULLET'
description = ' a very nice tournament with a lot a good players'

tournament23 = Tournament(name, location, date, rounds_count, rounds, players, time_control, description)

print(tournament23.__dict__)

print(Serializable.serialize(tournament23))


