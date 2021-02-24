# coding=utf-8

"""
File for different tests on the features of the class Match
"""

from models.serializable import Serializable
from models.match import Match
from models.player import Player


player1 = Player('aKONdé', 'Axel', '1986-05-02', Player.Gender.MALE, 1)
player2 = Player('Berd', 'Bernard', '1982-03-01', 'FEMALE', 3)

player1_score = 1
player2_score = 0


print("Start: Test Serialization/Deserialization Match")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
match1 = Match(player1, player2, player1_score, player2_score)
serialized_match1 = Match.serialize(match1)
print(match1.__dict__)  # pb print trouver comment afficher le detail des players en liste de dicts alors qu'on est dans une instance d'objet
print(serialized_match1)
assert match1.__dict__ == serialized_match1  #  le test ne fonctionne plus mais les données sont bonnes
print("End: Test Serialization/Deserialization Match")
