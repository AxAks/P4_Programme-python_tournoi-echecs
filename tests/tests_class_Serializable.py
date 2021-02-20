from models.serializable import Serializable
from models.players import Player


"""
File for different tests on the features of the project
"""


# Sample Values

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

players_dicts = [
    player1.__dict__, player2.__dict__,
    player3.__dict__, player4.__dict__,
    player5.__dict__, player6.__dict__,
    player7.__dict__, player8.__dict__,
    player9.__dict__, player10.__dict__
]

# Class Serializable
# Test Serialization / Deserialization
# Works in both directions

def test_serialize(_obj):
    return Serializable.serialize(_obj)


def test_deserialize(attributes_dict):
    _obj = Player(**attributes_dict)
    return _obj

print(" Test Serialization")

serialized_player1 = test_serialize(player1)
print(type(test_serialize(player1)))
print(test_serialize(player1))

print("Test Deserialization")
print(test_deserialize(serialized_player1))
print(test_deserialize(serialized_player1).__dict__)



def test_serialize_list_of_objects(_obj_dict_list):
    return Serializable.serialize_list_of_objects(_obj_dict_list)


print(test_serialize_list_of_objects(players_dicts))
