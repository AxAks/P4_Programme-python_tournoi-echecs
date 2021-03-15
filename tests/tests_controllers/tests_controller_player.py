# coding=utf-8

from controllers.controller import Creator
from controllers import controller
# from controllers import player_controller
# from controllers.player_controller import PlayerCreator
from models.player import Player
from tests import sample_values as test_sample

"""
File for different tests on the features of the player controller
"""


# instanciation des players

players_list = [test_sample.player1_dict,
                test_sample.player2_dict,
                test_sample.player3_dict,
                test_sample.player4_dict]

for player in players_list:
    controller.create_player(player)


# tests

print('--Player Registry--')
print("\n".join(Creator.player_registry))

player_ids = ['3be40089-64ff-48c2-8e6e-bc005ad378d2',
              'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b',
              '1bcb740a-3ca1-49e8-889f-30ca3c1bc293']

print('--List All Players Instances--')
for player_id in Creator.player_registry.keys():
    print(controller.get_by_id(player_id))

print('-- Get 1 Player Instance--')
print(controller.get_by_id('f'))
