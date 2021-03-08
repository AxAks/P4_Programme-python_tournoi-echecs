# coding=utf-8

from controllers import tournament_controller
from controllers.tournament_controller import TournamentCreator
from models.tournament import Tournament
from tests import sample_values as test_sample

"""
File for different tests on the features of the tournament controller
"""



# instanciation des Tournois

print("--Tournament Creation 1--")
print(TournamentCreator.create_tournament(test_sample.tournament35_dict))
print("--Tournament Creation 2--")
print(TournamentCreator.create_tournament(test_sample.tournament343_dict))
print("--Tournament Registry--")
print(Tournament.registry)
print("--Get 1 Tournament--")
print(TournamentCreator.get_tournament('Best Tournament Ever', 'Genève', '1987-02-28'))
