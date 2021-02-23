# coding=utf-8
"""
File for different tests on the features of the class Round
"""

from datetime import datetime

from models.serializable import Serializable
from models.players import Player
from models.tournaments import Tournament
from models.rounds import Round


# Sample Values

#  Player
player1 = Player('aKONdé', 'Axel', '1986-05-02', Player.Gender.MALE, 1)
player2 = Player('Berd', 'Bernard', '1982-03-01', 'FEMALE', 3)
player3 = Player('CERAS', 'Cédric', '1978-04-26', 'FEMALE', 2)
player4 = Player('Deflar', 'Didier', '1991-12-21', 'FEMALE', 4)

players_list = [player1, player2, player3, player4]

# Tournament
name = 'Best Tournament Ever'
location = 'Geneve'
date = '1987-02-28'
players = players_list
time_control = 'BULLET'
description = 'a very nice tournament with four outstanding players'
rounds_count = 0
rounds = 3

tournament24 = Tournament(name, location, date, players, time_control, description, rounds_count, rounds)


# Match

# Round

round1 = Round('Round 1', tournament24, matches=[], end_time=datetime.now())
round2 = Round('Round 2', tournament24, matches=[], end_time=datetime.now())
round3 = Round('Round 3', tournament24, matches=[], end_time=datetime.now())

print(round1)
print(round1.__dict__)
print(round2)
print(round2.__dict__)
print(round3)
print(round3.__dict__)


# Serialization / Deserialization
def test_serialize_round(round_object):
    return Round.serialize(round_object)


def test_deserialize_round(attributes_dict):
    _obj = Round(**attributes_dict)
    return _obj


print("Start: Test Serialization/Deserialization Round")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
serialized_round1 = test_serialize_round(round1)
deserialized_round1 = test_deserialize_round(serialized_round1)
print(round1)
print(round1.__dict__) # pb print trouver comment afficher le detail du tournoi sous forme de dict alors qu'on est dans une instance d'objet
print(deserialized_round1.__dict__)


assert round1.__dict__ == deserialized_round1.__dict__ # le test ne fonctionne plus mais les données sont bonnes

print("End: Test Serialization/Deserialization Round")
