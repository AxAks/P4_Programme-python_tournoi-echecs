# coding=utf-8

"""
File for different tests on the features of the tournament controller
"""

from controllers import tournament_controller
# from controllers.player_controller import PlayerCreator
from models.tournament import Tournament
from tests import sample_values as test_sample


# instanciation des Tournois

print("--Tournament Creation 1--")
print(tournament_controller.create_tournament(test_sample.tournament35_dict))
print("--Tournament Creation 2--")
print(tournament_controller.create_tournament(test_sample.tournament343_dict))
print("--Tournament Registry--")
print(Tournament.registry)
print("--Get 1 Tournament--")
print(tournament_controller.get_tournament('Best Tournament Ever', 'Genève', '1987-02-28'))
