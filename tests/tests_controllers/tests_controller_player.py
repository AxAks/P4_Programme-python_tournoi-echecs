# coding=utf-8

from controllers.player_controller import PlayerController
from models.player import Player
from tests import sample_values as test_sample

"""
File for different tests on the features of the player controller
"""


# instanciation des players

player1 = Player(**test_sample.player1_dict)
player2 = Player(**test_sample.player2_dict)
player3 = Player(**test_sample.player3_dict)
player4 = Player(**test_sample.player4_dict)


# tests

print(f'Player1: {player1.identifier}\nPlayer2: {player2.identifier}\n'
      f'Player3: {player3.identifier}\nPlayer4: {player4.identifier}')


for player in Player.instances:
      print(player.__dict__)
