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
    player_creator = Creator(Player)  # copié des tests, à voir si je peux en faire quelque chose







# infos pour la suite !
"""
# Pour enregistrer les instances crées dans une liste
# pour sérialiser toutes les instances de joueurs ensuite:

self.instances = [] if self.instances is None else self.instances.append(self) (dans la classe Player) # on laisse tomber ca du coup ?


# Pour sauvegarder plusieurs instances de joueurs serialisées dans TinyDB:
db = TinyDB(‘db.json’)
players_table = db.table(‘players’)
players_table.truncate()	# clear the table first
players_table.insert_multiple(serialized_players)

# Pour recharger les joueurs sérialisés, tu peux faire ceci
serialized_players = players_table.all()
"""