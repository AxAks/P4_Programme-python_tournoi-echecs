# coding=utf-8

from controllers.factory import Factory
from models.player import Player
from views.menus.player_menu import PlayerMenu

"""
Controller file for Player
"""

"""
Temp : Just for me !
Controller : link between Models (Classes) and Views
-  models updates
plusieurs fichiers controller à écrire : scinder
"""

# voir comment on gère SuperFactory, Factory, PlayerFactory, Tournament Factory : mise en place d'un Singleton ?


class PlayerFactory:
    """
    Subclass of Factory to create and manage Player instances
    à continuer ...
    """
    def player_factory(self):
        player_factory = Factory(Player)  # copié des tests, à voir si je peux en faire quelque chose
        return player_factory


class PlayerController(Player, PlayerMenu):
    def __init__(self):
        super().__init__()


# infos pour la suite !
"""
# Pour enregistrer les instances crées dans une liste
# pour sérialiser toutes les instances de joueurs ensuite:

player_factory.registry
tournament_factory.registry


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