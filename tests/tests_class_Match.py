# coding=utf-8

"""
File for different tests on the features of the class Match
"""

from models.serializable import Serializable
from models.match import Match
from models.player import Player

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

player1 = Player(**player1_dict)
player2 = Player(**player2_dict)


player1_score = 1
player2_score = 0


match1_dict = {
    'player1': {'uuid': 1, 'last_name': 'Akondé', 'first_name': 'Axel',
                'birthdate': '1986-05-02', 'gender': 'MALE', 'ranking': 2500},
    'player2': {'uuid': 2, 'last_name': 'Berd', 'first_name': 'Bernard',
                'birthdate': '1982-03-01', 'gender': 'MALE', 'ranking': 2400},
    'player1_score': 0,
    'player2_score': 0
}
match1_tuple = (
    [
        match1_dict['player1'],
        match1_dict['player1_score']
    ],
    [
        match1_dict['player2'],
        match1_dict['player2_score']
    ],
)


match1 = Match(**match1_dict)


serialized_match1 = Serializable.serialize(match1)
deserialized_match1 = Match(**serialized_match1)


print("Start: Test Serialization/Deserialization Match")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
serialized_match1 = Match.serialize(match1)
print(f'Match Tuple : {match1_tuple}')
print(f'Serialized Match 1 : {serialized_match1}')
assert match1_tuple == serialized_match1
print("End: Test Serialization/Deserialization Match")
