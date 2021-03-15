# coding=utf-8

from controllers.creator import Creator
from controllers.player_controller import PlayerCreator
# from controllers.player_controller import PlayerCreator
from models.player import Player
from tests import sample_values as test_sample

"""
File for different tests on the features of the player controller
"""


# instanciation des players


player_creator = Creator(Player)

players_list = [test_sample.player1_dict,
                test_sample.player2_dict,
                test_sample.player3_dict,
                test_sample.player4_dict]

for player in players_list:
    Creator.player_creator.create(**player)
    print('ici')

# tests

print('--Player Registry--')
for key in player_creator.registry:
    print(f"{key} : {player_creator.registry[key].first_name}")

player_ids = ['3be40089-64ff-48c2-8e6e-bc005ad378d2',
              'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b',
              '1bcb740a-3ca1-49e8-889f-30ca3c1bc293']

"""
print('--List All Players Instances--')
for player_id in player_creator.registry.keys():
    print(controller.get_by_id(player_id))

print('-- Get 1 Player Instance--')
print(controller.get_by_id('f'))
"""