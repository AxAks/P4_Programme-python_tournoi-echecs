# coding=utf-8

"""
File for different tests on the features of the tournament controller
"""

# from controllers.tournament_controller import TournamentCreator
from controllers.creator import Creator
from models.tournament import Tournament
from tests import sample_values as test_sample




tournament_creator = Creator(Tournament)

# instanciation des Tournois et ajout au registre
print("--Tournament Creation 1--")
print(tournament_creator.create(**test_sample.tournament35_dict))
print("--Tournament Creation 2--")
print(tournament_creator.create(**test_sample.tournament343_dict).identifier)
print("--Tournament Registry--")
print(tournament_creator.registry)
print("--Get 1 Tournament--")

"""
print(get_tournament('Ever'))
"""