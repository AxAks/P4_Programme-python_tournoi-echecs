# coding=utf-8
from models.player import Player
from models.tournament import Tournament
from tests import sample_values as test_sample
from controllers.supercreator import SuperCreator

from controllers.creator import Creator


"""
File for different tests on the features of the general controller
"""


# je veux une fonction générique qui :
# - crée tout type d'objets
# - tient un registre
# - permet de chercher un instance d'objet
# - s'appuie sur des subclasses specifiques à un type d'objet (Player/Tournament)
# -> Class Creator dans controller



# print(player_creator)

# Creation des Createurs d'objets
# player_creator = Creator(Player)  # je veux trouver un moyen d'enlever cette étape ! # SuperCreator
# tournament_creator = Creator(Tournament) # ici aussi

super_creator = SuperCreator()
print(super_creator)
player_creator = SuperCreator.create_creator(Player)


#super_creator = SuperCreator()
#SuperCreator.create_creator(Player)
#print(super_creator.creators)

"""
# Creation des objets
player1 = player_creator.create(**test_sample.player1_dict)
player2 = player_creator.create(**test_sample.player2_dict)
tournament35 = tournament_creator.create(**test_sample.tournament35_dict)
tournament343 = tournament_creator.create(**test_sample.tournament343_dict)

print(player1.identifier)
print(player2.identifier)
print(tournament35.__dict__)
print(player_creator.registry)
print(tournament_creator.registry)

print(player_creator.search('2'))
print(tournament_creator.search('Gen'))
"""


