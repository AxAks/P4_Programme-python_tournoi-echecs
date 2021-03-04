# coding=utf-8

"""
File for different tests on the features of the class Player
"""

from models.player import Player


# Class Player

# Sample Values
# Tests Player Objects Instantiation
# Setters / Getters


player1_dict = {
    'identifier': '3be40089-64ff-48c2-8e6e-bc005ad378d2',
    'last_name': 'aKONdé',
    'first_name': 'Axel',
    'birthdate': '1986-05-02',
    'gender': Player.Gender['MALE'],
    'ranking': 2500
}
player2_dict = {
    'identifier': 'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b',
    'last_name': 'Berd',
    'first_name': 'Bernard',
    'birthdate': '1983-03-01',
    'gender': 'MALE',
    'ranking': 2400
}

player3_dict = {
    'identifier': '4f4e8869-fbd2-48d7-b759-fafd725df22f',
    'last_name': 'CERAS',
    'first_name': 'Cédric',
    'birthdate': '1978-04-26',
    'gender': 'MALE',
    'ranking': 1400
}

player4_dict = {
    'identifier': '1bcb740a-3ca1-49e8-889f-30ca3c1bc293',
    'last_name': 'Deflar',
    'first_name': 'Didier',
    'birthdate': '1991-12-21',
    'gender': 'MALE',
    'ranking': 1300
}

player5_dict = {
    'identifier': 'f1d63919-1d15-4784-a724-5554dccdb076',
    'last_name': 'Edourd',
    'first_name': 'Emilie',
    'birthdate': '1922-05-01',
    'gender': 'FEMALE',
    'ranking': 1290
}

player6_dict = {
    'identifier': '6246d2f8-dab2-452e-b994-2c3e8aaedcef',
    'last_name': 'Ferrat',
    'first_name': 'Fanny',
    'birthdate': '1985-09-12',
    'gender': 'FEMALE',
    'ranking': 120
}

player7_dict = {
    'identifier': '6cd402fb-9e79-4e23-a326-5b7e215de205',
    'last_name': 'GRAND',
    'first_name': 'Gérard',
    'birthdate': '1982-03-01',
    'gender': 'MALE',
    'ranking': 1300
}

player8_dict = {
    'identifier': '96b0887a-58f0-4aa6-a68f-9b845a7c9ec1',
    'last_name': 'Harry',
    'first_name': 'Henriette',
    'birthdate': '1972-11-21',
    'gender': 'FEMALE',
    'ranking': 150
}

player9_dict = {
    'identifier': '23ed1860-bd10-42e1-b7b7-9b4c114a5d5c',
    'last_name': 'Isidore',
    'first_name': 'Isabelle',
    'birthdate': '1984-03-01',
    'gender': 'FEMALE',
    'ranking': 200
}

player10_dict = {
    'identifier': '11438f73-64b8-491b-8290-17548a794f58',
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
    return player_object.serialize()


def test_deserialize_player(attributes_dict):
    _obj = Player(**attributes_dict)
    return _obj


print("Start: Test Serialization/Deserialization Player")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
serialized_player2 = test_serialize_player(player2)  # ca commence a péter ici pour birthdate _pod
deserialized_player2 = test_deserialize_player(serialized_player2)
print(f'Dict: {player2_dict}')
print(f'Object: {player2.__dict__}')
print(f'Serialized: {serialized_player2}')
assert player2_dict == serialized_player2
print("End: Test Serialization/Deserialization Player")
print(player1.last_name, player1.identifier)
print(player2.last_name, player2.identifier)
print(player3.last_name, player3.identifier)
print(player4.last_name, player4.identifier)
print(player5.last_name, player5.identifier)
print(player6.last_name, player6.identifier)
print(player7.last_name, player7.identifier)
print(player8.last_name, player8.identifier)
print(player9.last_name, player9.identifier)
print(player10.last_name, player10.identifier)
