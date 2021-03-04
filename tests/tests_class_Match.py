# coding=utf-8

"""
File for different tests on the features of the class Match
"""

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

"""
player1 = Player(**player1_dict)
player2 = Player(**player2_dict)


player1_score = 1
player2_score = 0
"""
match1_dict = {
    'player1': {'identifier': '3be40089-64ff-48c2-8e6e-bc005ad378d2', 'last_name': 'Akondé', 'first_name': 'Axel',
                'birthdate': '1986-05-02', 'gender': 'MALE', 'ranking': 2500},
    'player2': {'identifier': 'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b', 'last_name': 'Berd', 'first_name': 'Bernard',
                'birthdate': '1982-03-01', 'gender': 'MALE', 'ranking': 2400},
    'player1_score': 1.0,
    'player2_score': 0.0
}
# résultats possibles d'un match :
# 1.0 - 0.0
# 0.5 -  0.5
# 0.0 - 1.0

"""
match1 = Match(**match1_dict)
serialized_match1 = serialize(match1)
deserialized_match1 = Match(**serialized_match1)
serialized_match1 = serialize(match1)
match1_tuple = Match.get_match_as_tuple(match1)

print("Start: Test Serialization/Deserialization Match")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
print(f' Match 1 Dict : {match1.__dict__}')
print(f' Match 1 Object  : {match1.__dict__}')
print(f'Serialized Match 1 : {serialized_match1}')
print(f'Match Tuple : {match1_tuple}')
print(f'Match Tuple Type : {type(match1_tuple)}')
print("End: Test Serialization/Deserialization Match")
"""

print(f'Match Dict: {match1_dict}')
match_test_obj = Match(**match1_dict)
print(f'Match Object Dict: {match_test_obj.__dict__}')
match_test_serialized = match_test_obj.serialize()
print(f'Deserialized Match: {match_test_serialized}')
match_test_tuple = match_test_obj.get_match_as_tuple()
print(f'Match Tuple: {match_test_tuple}')
assert match1_dict == match_test_serialized
