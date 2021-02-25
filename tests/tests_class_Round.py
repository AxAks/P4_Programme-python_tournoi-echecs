# coding=utf-8
"""
File for different tests on the features of the class Round
"""

from datetime import datetime

from models.serializable import Serializable
from models.player import Player
from models.tournament import Tournament
from models.round import Round


# Sample Values

#  Player
player1_dict = {
    'uuid': 1,
    'last_name': 'aKONdé',
    'first_name': 'Axel',
    'birthdate': '1986-05-02',
    'gender': Player.Gender.MALE,
    'ranking': 2500
}
player2_dict = {
    'uuid': 2,
    'last_name': 'Berd',
    'first_name': 'Bernard',
    'birthdate': '1982-03-01',
    'gender': 'MALE',
    'ranking': 2400
}

player3_dict = {
    'uuid': 3,
    'last_name': 'CERAS',
    'first_name': 'Cédric',
    'birthdate': '1978-04-26',
    'gender': 'MALE',
    'ranking': 1400
}

player4_dict = {
    'uuid': 4,
    'last_name': 'Deflar',
    'first_name': 'Didier',
    'birthdate': '1991-12-21',
    'gender': 'MALE',
    'ranking': 1300
}

player1 = Player(**player1_dict)
player2 = Player(**player2_dict)
player3 = Player(**player3_dict)
player4 = Player(**player4_dict)

players_list = [player1, player2, player3, player4]

# Tournament
name = 'Best Tournament Ever'
location = 'Geneve'
date = '1987-02-28'
players = players_list
time_control = 'BULLET'
description = 'a very nice tournament with four outstanding players'
rounds_list = []
rounds = 3

tournament24 = Tournament(name, location, date, players, time_control, description, rounds_list, rounds)


# Match

player1_score = 1
player2_score = 0
player3_score = 0.5
player4_score = 0.5


match1 = (player1, player2, player1_score, player2_score)
match2 = (player3, player4, player3_score, player4_score)

matches_list = [match1, match2]


# Round

round1_dict = {
    'name': 'Round 1',
    'tournament': tournament24,
    'matches': matches_list,
    'end_time': datetime.now()
}

round1 = Round(**round1_dict)
print(round1)
print(round1.__dict__)


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
print(f'Round 1 Object : {round1}')
print(f'Round 1 Object Details{round1_dict}') # pb print trouver comment afficher le detail du tournoi sous forme de dict alors qu'on est dans une instance d'objet
print(f'Round 1 serialized {deserialized_round1.__dict__}')


assert round1_dict == deserialized_round1.__dict__ # le test ne fonctionne plus mais les données sont bonnes

print("End: Test Serialization/Deserialization Round")
