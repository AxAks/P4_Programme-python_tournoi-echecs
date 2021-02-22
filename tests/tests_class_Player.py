# coding=utf-8

"""
File for different tests on the features of the class Player
"""

from models.serializable import Serializable
from models.players import Player



# Class Player

# Sample Values
# Tests Player Objects Instantiation
# Setters / Getters

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

players = [
    player1, player2,
    player3, player4,
    player5, player6,
    player7, player8,
    player9, player10
]


# Tests Serialization/Deserialization
def test_serialize_player(player_object):
    return Serializable.serialize(player_object)


def test_deserialize_player(attributes_dict):
    _obj = Player(**attributes_dict)
    return _obj


print("Start: Test Serialization/Deserialization Player")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
serialized_player2 = test_serialize_player(player2)
deserialized_player2 = test_deserialize_player(serialized_player2)
assert player2.__dict__ == deserialized_player2.__dict__
print("End: Test Serialization/Deserialization Player")


