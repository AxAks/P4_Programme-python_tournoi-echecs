# coding=utf-8

"""
File for different tests on the features of the tournament controller
"""

from controllers import tournament_controller
# from controllers.player_controller import PlayerCreator
from models.tournament import Tournament
from tests import sample_values as test_sample


# instanciation des Tournois

print(tournament_controller.create_tournament(test_sample.tournament35_dict).__dict__)
print(tournament_controller.create_tournament(test_sample.tournament343_dict).__dict__)
print(tournament_controller.get_tournament('2021-02-28'))
print(Tournament.registry)
