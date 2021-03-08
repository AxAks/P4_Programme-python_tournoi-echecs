# coding=utf-8
from controllers.controller import create_tournament, get_tournament
from models.player import Player

from controllers import tournament_controller, controller
from controllers.tournament_controller import TournamentCreator
from models.tournament import Tournament
from tests import sample_values as test_sample

"""
File for different tests on the features of the tournament controller
"""



# instanciation des Tournois et ajout au registre



print("--Tournament Creation 1--")
print(create_tournament(test_sample.tournament35_dict))
print("--Tournament Creation 2--")
print(create_tournament(test_sample.tournament343_dict))
print("--Tournament Registry--")
print(Tournament.registry)
print("--Get 1 Tournament--")
print(controller.get_tournament('Best Tournament Ever 20', 'Genève', '2021-02-28', '2021-02-28').__dict__)
