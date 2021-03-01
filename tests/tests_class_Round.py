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
dates = '1987-02-28'
players = players_list
time_control = 'BULLET'
description = 'a very nice tournament with four outstanding players'
rounds_list = []
rounds = 3

# tournament24 = Tournament(name, location, dates, players, time_control, description, rounds_list, rounds) # pb car 9 args au lieu d'un seul accepté (dict)!

#  Match

player1_score = 1
player2_score = 0
player3_score = 0.5
player4_score = 0.5

match1 = (player1, player2, player1_score, player2_score)
match2 = (player3, player4, player3_score, player4_score)

matches_list = [match1, match2]


#  Round
round1_dict = {
    'name': 'Round 1',
    'tournament': {
        'name': 'Tournament 24 Best Tournament Ever',
        'location': 'Geneve',
        'dates': '1987-02-28',
        'players': [
            {'uuid': 1, 'last_name': 'Akondé', 'first_name': 'Axel', 'birthdate': '1986-05-02', 'gender': 'MALE',
             'ranking': 2500},
            {'uuid': 2, 'last_name': 'Berd', 'first_name': 'Bernard', 'birthdate': '1982-03-01', 'gender': 'MALE',
             'ranking': 2400},
            {'uuid': 3, 'last_name': 'Ceras', 'first_name': 'Cédric', 'birthdate': '1978-04-26', 'gender': 'MALE',
             'ranking': 1400},
            {'uuid': 4, 'last_name': 'Deflar', 'first_name': 'Didier', 'birthdate': '1991-12-21', 'gender': 'MALE',
             'ranking': 1300}
        ],
        'time_control': 'BULLET',
        'description': 'a very nice tournament with four outstanding players',
        'rounds_list': [],
        'rounds': 3,
    },
    'matches': [
        (
            [{'uuid': 1, 'last_name': 'Akondé', 'first_name': 'Axel', 'birthdate': '1986-05-02', 'gender': 'MALE',
              'ranking': 2500}, 1],
            [{'uuid': 2, 'last_name': 'Berd', 'first_name': 'Bernard', 'birthdate': '1982-03-01', 'gender': 'MALE',
              'ranking': 2400}, 0]),
        (
            [{'uuid': 3, 'last_name': 'Ceras', 'first_name': 'Cédric', 'birthdate': '1978-04-26', 'gender': 'MALE',
              'ranking': 1400}, 0.5],
            [{'uuid': 4, 'last_name': 'Deflar', 'first_name': 'Didier', 'birthdate': '1991-12-21', 'gender': 'MALE',
              'ranking': 1300}, 0.5]
        )
    ],
    'start_time': '2021-02-26T11:33:07',
    'end_time': '2021-02-26T11:34:07'
}

round1 = Round(**round1_dict)


# Serialization / Deserialization
def test_serialize_round(round_object):
    return Serializable.serialize(round_object)


def test_deserialize_round(attributes_dict):
    _obj = Round(**attributes_dict)
    return _obj


print("Start: Test Serialization/Deserialization Round")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")

serialized_round1 = test_serialize_round(round1)
deserialized_round1 = test_deserialize_round(serialized_round1)
print(f'ICI -> Round 1 Dict : {round1_dict}')
print(f'Round 1 Object : {round1}')
print(f'Round 1 Object Details{round1.__dict__}')
print(f'ICI -> Round 1 serialized {serialized_round1}')
print(f'Round 1 deserialized {deserialized_round1.__dict__}')
assert round1_dict == serialized_round1  #  le test ne fonctionne plus mais les données sont bonnes
assert round1.__dict__ == deserialized_round1.__dict__
print("End: Test Serialization/Deserialization Round")
