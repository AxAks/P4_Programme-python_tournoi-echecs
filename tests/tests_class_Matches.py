# coding=utf-8

"""
File for different tests on the features of the class Match
"""

from models.serializable import Serializable
from models.matches import Match
from models.players import Player


player1 = Player('aKONdé', 'Axel', '1986-05-02', Player.Gender.MALE, 1)
player2 = Player('Berd', 'Bernard', '1982-03-01', 'FEMALE', 3)

player1_score = 1
player2_score = 0

match1 = Match(player1, player2, player1_score, player2_score)
serialized_match1 = Match.serialize(match1)
print(match1.__dict__)
print(serialized_match1)

