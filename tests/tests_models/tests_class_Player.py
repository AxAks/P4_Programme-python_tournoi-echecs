# coding=utf-8

"""
File for different tests on the features of the class Player
"""

from models.player import Player
from tests import sample_values as test_sample


# Tests Player Objects Instantiation
# Setters / Getters
player1 = Player(**test_sample.player1_dict)
player2 = Player(**test_sample.player2_dict)
player3 = Player(**test_sample.player3_dict)
player4 = Player(**test_sample.player4_dict)
player5 = Player(**test_sample.player5_dict)
player6 = Player(**test_sample.player6_dict)
player7 = Player(**test_sample.player7_dict)
player8 = Player(**test_sample.player8_dict)
player9 = Player(**test_sample.player9_dict)
player10 = Player(**test_sample.player10_dict)


players = [
    player1, player2,
    player3, player4,
    player5, player6,
    player7, player8,
    player9, player10
]


# Tests Serialization/Deserialization
def test_serialize_player(player_object):
    return player_object.serialize()


def test_deserialize_player(attributes_dict):
    _obj = Player(**attributes_dict)
    return _obj


serialized_player2 = test_serialize_player(player2)
deserialized_player2 = test_deserialize_player(serialized_player2)

print("Start: Test Serialization/Deserialization Player")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
print(f'Dict: {test_sample.player2_dict}')
print(f'Object: {player2.__dict__}')
print(f'Serialized: {serialized_player2}')

assert test_sample.player2_dict == serialized_player2
print("End: Test Serialization/Deserialization Player")
