# coding=utf-8

"""
File for different tests on the features of the class Tournament
"""

from models.serializable import Serializable
from models.tournaments import Tournament
from models.players import Player


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


# Tests Serialization/Deserialization Tournament
def test_serialize_tournament(tournament_object):
    return Serializable.serialize(tournament_object)


def test_deserialize_tournament(attributes_dict):
    _obj = Tournament(**attributes_dict)
    return _obj


print("Start: Test Serialization/Deserialization Tournament")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
serialized_tournament24 = test_serialize_tournament(tournament24)
deserialized_tournament24 = test_deserialize_tournament(serialized_tournament24)
assert tournament24.__dict__ == deserialized_tournament24.__dict__
print("End: Test Serialization/Deserialization Tournament")
