# coding=utf-8

from models.player import Player
from models.tournament import Tournament
from tests import sample_values as test_sample
from models.superfactory import super_factory as sf


"""
File for different tests on the features of the general controller
"""

# Creation des contructeurs d'objets via SuperFactory
player_factory = sf.create_factory(Player)
tournament_factory = sf.create_factory(Tournament)

# Creation des objets via Factory
player1 = player_factory.create(**test_sample.player1_dict)
player2 = player_factory.create(**test_sample.player2_dict)
player1copy = player_factory.create(**test_sample.player1_dict)
tournament35 = tournament_factory.create(**test_sample.tournament35_dict)
tournament343 = tournament_factory.create(**test_sample.tournament343_dict)
tournament343copy = tournament_factory.create(**test_sample.tournament343_dict)

print(f"Player1 ID: {player1.identifier}")
print(f"Player2 ID: {player2.identifier}")
print(player1copy.identifier)
print(f"Tournament 35: {tournament35.__dict__}")
print(f"Registre Joueurs: {player_factory.registry}")
print(f"Registre Tournois:{tournament_factory.registry}")
print(f"Recherche 1 (Player): {player_factory.search('ff')}")
print(f"Recherche 2 (Tournament): {tournament_factory.search('Gen')}")


# Serialisation des instances
serialized_player_instances = [player_factory.registry[key].serialize() for key in player_factory.registry]
[print(serialized_player_instance) for serialized_player_instance in serialized_player_instances]

serialized_tournament_instances = [tournament_factory.registry[key].serialize() for key in tournament_factory.registry]
[print(serialized_tournament_instance) for serialized_tournament_instance in serialized_tournament_instances]
