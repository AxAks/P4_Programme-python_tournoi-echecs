# coding=utf-8

"""
File for different tests on the features of the class Match
"""

from models.serializable import Serializable
from models.match import Match
from models.player import Player

from constants import INDEX_PLAYER1, INDEX_PLAYER2, INDEX_PLAYER1_SCORE, INDEX_PLAYER2_SCORE
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

player1 = Player(**player1_dict)
player2 = Player(**player2_dict)


player1_score = 1
player2_score = 0




# fait bloquer serialize car on passe les players en dict et non en tant qu'objet
match1_dict = {
    'player1': {'uuid': 1, 'last_name': 'Akondé', 'first_name': 'Axel',
                'birthdate': '1986-05-02', 'gender': 'MALE', 'ranking': 2500},
    'player2': {'uuid': 2, 'last_name': 'Berd', 'first_name': 'Bernard',
                'birthdate': '1982-03-01', 'gender': 'MALE', 'ranking': 2400},
    'player1_score': 1,
    'player2_score': 0
}
match1_tuple =(
    [
        match1_dict['player1'],
        match1_dict['player1_score']
    ],
    [
        match1_dict['player2'],
        match1_dict['player2_score']
    ],
)

match1 = Match(**match1_dict)

print("Start: Test Serialization/Deserialization Match")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
serialized_match1 = Match.serialize(match1)
print(match1_tuple)  # pb print trouver comment afficher le detail des players en liste de dicts alors qu'on est dans une instance d'objet
print(serialized_match1)
assert match1_tuple == serialized_match1  #  le test ne fonctionne plus mais les données sont bonnes
print("End: Test Serialization/Deserialization Match")
