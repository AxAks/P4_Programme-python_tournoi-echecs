from models.players import Player, PlayerEncoder

from constants import MALE, FEMALE

"""
File for differents tests on the features of the project
"""

# Class Player

# Sample Values
player1 = Player('Akondé', 'Axel', '02/05/1896', MALE, 1)
player2 = Player('Berd', 'Bernard', '01/03/1982', MALE, 3)
player3 = Player('CERAS', 'Cédric', '26/04/1978', MALE, 2)
player4 = Player('Deflar', 'Didier', '21/12/1991', MALE, 4)
player5 = Player('Edourd', 'Emilie', '01/05/1922', FEMALE, 10)
player6 = Player('Ferrat', 'Fanny', '12/09/1985', FEMALE, 9)
player7 = Player('GRAND', 'Gérard', '01/03/1982', MALE, 7)
player8 = Player('Harry', 'Henriette', '21/11/1972', FEMALE, 8)
player9 = Player('Isidore', 'Isabelle', '01/03/1984', FEMALE, 6)
player10 = Player('Junot', 'Juliette', '01/03/1982', FEMALE, 5)

players = [
    player1, player2,
    player3, player4,
    player5, player6,
    player7, player8,
    player9, player10
]


# Tests Serialization
def test_serialize_one_player(player):
    print(PlayerEncoder(player).serialize_one_player(player))


def test_serialize_players(players):
    print(PlayerEncoder(players).serialize_players(players))


test_serialize_one_player(player2)
test_serialize_players(players)

"""
# Tests Deserialization

player1 = {}
player2 = {}
player3 = {}
player4 = {}
player5 = {}
player6 = {}
player7 = {}
player8 = {}
player9 = {}
player10 = {}
"""