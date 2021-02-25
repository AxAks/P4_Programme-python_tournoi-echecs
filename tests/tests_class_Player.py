# coding=utf-8

"""
File for different tests on the features of the class Player
"""

from models.serializable import Serializable
from models.player import Player



# Class Player

# Sample Values
# Tests Player Objects Instantiation
# Setters / Getters


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

player5_dict = {
    'uuid': 5,
    'last_name': 'Edourd',
    'first_name': 'Emilie',
    'birthdate': '1922-05-01',
    'gender': 'FEMALE',
    'ranking': 1290
}

player6_dict = {
    'uuid': 6,
    'last_name': 'Ferrat',
    'first_name': 'Fanny',
    'birthdate': '1985-09-12',
    'gender': 'FEMALE',
    'ranking': 120
}

player7_dict = {
    'uuid': 7,
    'last_name': 'GRAND',
    'first_name': 'Gérard',
    'birthdate': '1982-03-01',
    'gender': 'MALE',
    'ranking': 1300
}

player8_dict = {
    'uuid': 8,
    'last_name': 'Harry',
    'first_name': 'Henriette',
    'birthdate': '1972-11-21',
    'gender': 'FEMALE',
    'ranking': 150
}

player9_dict = {
    'uuid': 9,
    'last_name': 'Isidore',
    'first_name': 'Isabelle',
    'birthdate': '1984-03-01',
    'gender': 'FEMALE',
    'ranking': 200
}

player10_dict = {
    'uuid': 10,
    'last_name': 'Junot',
    'first_name': 'Juliette',
    'birthdate': '1982-03-01',
    'gender': 'FEMALE',
    'ranking': 500
}


player1 = Player(**player1_dict)
player2 = Player(**player2_dict)
player3 = Player(**player3_dict)
player4 = Player(**player4_dict)
player5 = Player(**player5_dict)
player6 = Player(**player6_dict)
player7 = Player(**player7_dict)
player8 = Player(**player8_dict)
player9 = Player(**player9_dict)
player10 = Player(**player10_dict)


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

