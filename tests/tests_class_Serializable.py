# coding=utf-8

"""
File for different tests on the features of the class Serializable
"""

from models.serializable import Serializable
from models.players import Player
from models.tournaments import Tournament
import sys

# Sample Values

# Player

player1 = Player('aKONdé', 'Axel', '1986-05-02', Player.Gender.MALE, 1)
player2 = Player('Berd', 'Bernard', '1982-03-01', 'FEMALE', 3)
player3 = Player('CERAS', 'Cédric', '1978-04-26', 'FEMALE', 2)
player4 = Player('Deflar', 'Didier', '1991-12-21', 'FEMALE', 4)
player5 = Player('Edourd', 'Emilie', '1922-05-01', 'FEMALE', 10)
player6 = Player('Ferrat', 'Fanny', '1985-09-12', 'FEMALE', 9)
player7 = Player('GRAND', 'Gérard', '1982-03-01', 'FEMALE', 7)
player8 = Player('Harry', 'Henriette', '1972-11-21', 'FEMALE', 8)
player9 = Player('Isidore', 'Isabelle', '1984-03-01', 'FEMALE', 6)
player10 = Player('Junot', 'Juliette', '1982-03-01', 'FEMALE', 5)

players_list = [
    player1, player2,
    player3, player4,
    player5, player6,
    player7, player8,
    player9, player10
]

# Tournament

name = 'Best Tournament Ever'
location = 'Geneve'
date = '1987-02-28'
players = [player1, player2, player3, player4]
time_control = 'BULLET'
description = 'a very nice tournament with a lot a good players'
rounds_count = 0
rounds = 3


tournament23 = Tournament(name, location, date, players, time_control, description, rounds_count, rounds)


# Class Serializable
# Test Serialization / Deserialization General
# Works in both directions


def test_serialize_global(_obj):
    return Serializable.serialize(_obj)


def test_deserialize_global(_obj_class, attributes_dict):
    _obj = _obj_class(**attributes_dict)
    return _obj


print("Start: Test Serialization/Deserialization Global")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
serialized_tournament23 = test_serialize_global(tournament23)
deserialized_tournament23 = test_deserialize_global(Tournament, serialized_tournament23)
assert tournament23.__dict__ == deserialized_tournament23.__dict__  # pb possible avec le stockage des players ? c'esst l'object player qui est stocké et non les infos du player
print("End: Test Serialization/Deserialization Global")


"""
# attempt to serialize a list of objects 
def test_serialize_list_of_objects(_objs_list):
    return Serializable.serialize_list_of_objects(_objs_list)


print(test_serialize_list_of_objects(players_list))
"""