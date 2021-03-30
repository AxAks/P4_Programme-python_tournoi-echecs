# coding=utf-8

from models.models_utils.factory import Factory
from models.player import Player
from tests import sample_values as test_sample

"""
File for different tests on the features of the player controller
"""


# instanciation des players


player_factory = Factory(Player)

players_list = [test_sample.player1_dict,
                test_sample.player2_dict,
                test_sample.player3_dict,
                test_sample.player4_dict]

for player_dict in players_list:
    player = player_factory.create(**player_dict)
    print(player)

# tests

print('--Player Registry--')
for key in player_factory.registry:
    print(f"{key} : {player_factory.registry[key].first_name}")

print('-- Get Matching Player Instance--')
print(player_factory.search('ce'))
