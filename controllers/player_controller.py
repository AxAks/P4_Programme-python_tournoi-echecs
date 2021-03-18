# coding=utf-8

from controllers.creator import Creator
from models.player import Player

"""
Controller file for Player
"""

"""
Temp : Just for me !
Controller : link between Models (Classes) and Views
-  models updates
plusieurs fichiers controller à écrire : scinder
"""

# Use Factory Method
# methode factory (voir tuto design pattern)
# voir controller directement : Class Creator


class PlayerCreator:
    """
    Subclass of Creator to create and manage Player instances
    à continuer ...
    """
    def player_creator(self):
        player_creator = Creator(Player)  # copié des tests, à voir si je peux en faire quelque chose
        return player_creator


# infos pour la suite !
"""
# Pour enregistrer les instances crées dans une liste
# pour sérialiser toutes les instances de joueurs ensuite:

player_creator.registry
tournament_creator.registry


serialized_instances = []
for key in registry:
    serialized_instance = registry[key].serialize()
    serialized_instances.append(serialized_instance)
return serialized_instances

# Pour sauvegarder plusieurs instances de joueurs serialisées dans TinyDB:
db = TinyDB(‘db.json’)
players_table = db.table(‘players’)
players_table.truncate()	# clear the table first
players_table.insert_multiple(serialized_players)

# Pour recharger les joueurs sérialisés, tu peux faire ceci
serialized_players = players_table.all()
"""