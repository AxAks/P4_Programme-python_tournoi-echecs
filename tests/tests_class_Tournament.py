# coding=utf-8

"""
File for different tests on the features of the class Tournament
"""

from models.tournament import Tournament
from models.player import Player


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
# pb assert

#  ecrire un dictionnaire des données et c'est ca qu'on comparera à deserialized_tournament24 !

tournament24_dict = {
    'tournament_name': 'Best Tournament Ever',
    'location': 'Geneve',
    'dates': '1987-02-28',
    'players': [
            {'player_uuid': '3be40089-64ff-48c2-8e6e-bc005ad378d2', 'last_name': 'Akondé', 'first_name': 'Axel',
             'birthdate': '1986-05-02', 'gender': 'MALE', 'ranking': 2500},
            {'player_uuid': 'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b', 'last_name': 'Berd', 'first_name': 'Bernard',
             'birthdate': '1982-03-01', 'gender': 'MALE', 'ranking': 2400},
            {'player_uuid': '4f4e8869-fbd2-48d7-b759-fafd725df22f', 'last_name': 'Ceras', 'first_name': 'Cédric',
             'birthdate': '1978-04-26', 'gender': 'MALE', 'ranking': 1400},
            {'player_uuid': '1bcb740a-3ca1-49e8-889f-30ca3c1bc293', 'last_name': 'Deflar', 'first_name': 'Didier',
             'birthdate': '1991-12-21', 'gender': 'MALE', 'ranking': 1300}],
    'time_control': 'BULLET',
    'description': 'a very nice tournament with four outstanding players',
    'rounds_list': [],
    'rounds': 3
}
tournament24 = Tournament(**tournament24_dict)


# Tests Serialization/Deserialization Tournament
def test_serialize_tournament(tournament_object):
    return tournament_object.serialize()


def test_deserialize_tournament(attributes_dict):
    _obj = Tournament(**attributes_dict)
    return _obj


print("Start: Test Serialization/Deserialization Tournament")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
serialized_tournament24 = test_serialize_tournament(tournament24)
deserialized_tournament24 = test_deserialize_tournament(serialized_tournament24)
print(f'Dict: {tournament24_dict}')
print(f'Object: {deserialized_tournament24.__dict__}')
print(f'Serialized: {serialized_tournament24}')
assert tournament24_dict == serialized_tournament24  # le test ne fonctionne plus mais les données sont bonnes
print("End: Test Serialization/Deserialization Tournament")
