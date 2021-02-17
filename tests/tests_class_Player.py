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

# Tests Serialization


# Tests Deserialization
