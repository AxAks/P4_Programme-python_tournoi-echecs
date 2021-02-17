from models.players import Player, PlayerEncoder


"""
File for differents tests on the features of the project
"""

#  Class Player

MALE = 'Male'
FEMALE = 'Female'


#  Sample Values
# Tests Player Objects Instantiation
# Setters / Getters

player1 = Player('Akondé', 'Axel', '1986/05/02', MALE, 1)
player2 = Player('Berd', 'Bernard', '1982/03/01', MALE, 3)
player3 = Player('CERAS', 'Cédric', '1978/04/26', MALE, 2)
player4 = Player('Deflar', 'Didier', '1991/12/21', MALE, 4)
player5 = Player('Edourd', 'Emilie', '1922/05/01', FEMALE, 10)
player6 = Player('Ferrat', 'Fanny', '1985/09/12', FEMALE, 9)
player7 = Player('GRAND', 'Gérard', '1982/03/01', MALE, 7)
player8 = Player('Harry', 'Henriette', '1972/11/21', FEMALE, 8)
player9 = Player('Isidore', 'Isabelle', '1984/03/01', FEMALE, 6)
player10 = Player('Junot', 'Juliette', '1982/03/01', FEMALE, 5)

players = [
    player1, player2,
    player3, player4,
    player5, player6,
    player7, player8,
    player9, player10
]







"""
# Tests Serialization
def test_serialize_one_player(player: dict):
    assert str(PlayerEncoder(player).serialize_one_player(player)) == "{'_Player__last_name': 'Berd', '_Player__first_name': 'Bernard', '_Player__birthdate': '01/03/1982', '_Player__gender': 'Male', '_Player__ranking': 3}"

def test_dump_serialized_player(player: dict):
    print(PlayerEncoder(player).dump_serialized_player(player))


def test_save_serialized_player_to_file(player: dict):
    PlayerEncoder(player).save_serialized_player_to_file(player)


def test_serialize_players(players: list):
    print(PlayerEncoder(players).serialize_players(players))


def test_dump_list_of_serialized_players(players: list):
    print(PlayerEncoder(players).dump_list_of_serialized_players(players))


def test_save_list_of_serialized_players_to_file(players: list):
    PlayerEncoder(players).save_list_of_serialized_players_to_file(players)


test_serialize_one_player(player2)
test_dump_serialized_player(player2)
test_save_serialized_player_to_file(player2)
test_serialize_players(players)
test_dump_list_of_serialized_players(players)
test_save_list_of_serialized_players_to_file(players)


# Tests Deserialization
# (...)


def test_load_player(player_string):
    PlayerDecoder.load_player(player_string)


def test_deserialize_one_player(input_file):
    input_file = 'serialized_player.json'
    PlayerDecoder.deserialize_one_player(input_file)


player2_string = '{"_Player__last_name": "Berd",' \
                 ' "_Player__first_name": "Bernard",' \
                 ' "_Player__birthdate": "01/03/1982",' \
                 ' "_Player__gender": "Male",' \
                 ' "_Player__ranking": 3}'

print(test_load_player(player2_string))
# print(test_deserialize_one_player(input_file='serialized_player.json'))
"""