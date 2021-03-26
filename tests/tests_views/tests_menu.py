# coding=utf-8

"""
Test file for menus
"""

from tests import sample_values as test_sample
from models.superfactory import super_factory as sf
from models.player import Player
from models.tournament import Tournament
from views.inputs import generic_inputs

# Mise en place des factories au démarrage
player_factory = sf.create_factory(Player)
tournament_factory = sf.create_factory(Tournament)

# load_state() , à partir d'un fichier normalement ! test sample // fichier formaté db.json
## simuler la fonction load : remplir les factories

# Vérif SuperFactories 1 : - que les factories sont créées et vides
print(sf.factories[Player].registry)
print(sf.factories[Tournament].registry)

# on instancie les players et les tournaments (ca instancie les rounds et les matchs qui vivent dans Tournament)
[player_factory.create(**player_dict) for player_dict in test_sample.players_list]
[tournament_factory.create(**tournament_dict) for tournament_dict in test_sample.tournaments_list]

# Verif du contenu des regitres players et tournament
p = 0
for player in player_factory.registry:
    p += 1
t = 0
for tournament in tournament_factory.registry:
    t += 1
print(f"---\n"
      f"-> {p} players imported\n"
      f"-> {t} tournaments imported\n"
      f"---")
print(sf.factories[Player].registry)  #  Verif
print(sf.factories[Tournament].registry)  #  Verif

# Verif de la création des Objets Round et Matches
round_list = \
    sf.factories[Tournament].registry['Best Tournament Ever , Genève , 1987-01-21 , 1987-01-22'].rounds_list
print(round_list)
for _round in round_list:
    print(_round.__dict__)
    for match in _round.matches:
        print(match.__dict__)
print('---')

# Inputs/Prints

generic_inputs.search_one_player()
