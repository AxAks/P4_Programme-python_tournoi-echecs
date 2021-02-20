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
# Test Serialization / Deserialization

"""
# A lot of back and forth processing to test
player1 = Player('Dupont', 'Jean', '1985-02-02', 'MALE', 2)
print("1ere instance de Player 1 objet")
print(f"Objet Player 1 : {player1.__dict__}")
print("...")

serialized_player1 = player1.serialize()
print(f"Serialized Player 1: {serialized_player1}")
print("...")

print(f"On reset le Player 1 en tant que dict (résultat obtenu)")
print("...")

player1_dict = {'last_name': 'Dupont', 'first_name': 'Jean', 'birthdate': '1985-02-02', 'gender': 'MALE', 'ranking': 2}
player1_obj = Player(**player1_dict)
print(f"Deserialized Player 1: {player1_obj.__dict__}")
print("...")

print("On re-serialise le Player 1 à partir de Player1_obj (Deserialized Player 1)")
serialized_player1_second = player1_obj.serialize()
print(f"2eme serialisation de player 1: {serialized_player1_second}")
print("...")

print("On re-deserialise le Player 1 à partir de Player1_obj (Deserialized Player 1)")
player1_dict_second = {'last_name': 'Dupont', 'first_name': 'Jean', 'birthdate': '1985-02-02', 'gender': 'MALE', 'ranking': 2}
player1_obj_2 = Player(**player1_dict_second)
print(f"2eme deserialisation de player 1: {player1_obj_2.__dict__}")
"""


def test_serialize(_obj):
    return Serializable.serialize(_obj)


def test_deserialize(attributes_dict):
    _obj = Player(**attributes_dict)
    return _obj


def test_serialize_list_of_objects(_obj_dict_list):
    return Serializable.serialize_list_of_objects(_obj_dict_list)


serialized_player1 = test_serialize(player1)
print(type(test_serialize(player1)))
print(test_serialize(player1))

print(test_deserialize(serialized_player1))
print(test_deserialize(serialized_player1).__dict__)


print(test_serialize_list_of_objects(players_dicts))
