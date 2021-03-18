# coding=utf-8

"""
File for different tests on the features of the tournament controller
"""

# from controllers.tournament_controller import TournamentFactory
from controllers.factory import Factory
from models.tournament import Tournament
from tests import sample_values as test_sample




tournament_factory = Factory(Tournament)

# instanciation des Tournois et ajout au registre
print("--Tournament Creation 1--")
print(tournament_factory.create(**test_sample.tournament35_dict))
print("--Tournament Creation 2--")
print(tournament_factory.create(**test_sample.tournament343_dict).identifier)
print("--Tournament Registry--")
print(tournament_factory.registry)
print("--Get 1 Tournament--")

"""
print(get_tournament('Ever'))
"""