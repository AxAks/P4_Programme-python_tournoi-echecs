# coding=utf-8

import gc

from controllers.controller import Creator
from models.player import Player
from tinydb import TinyDB


"""
Controller file for Player
"""
"""
Temp : Just for me !
Controller : link between Models (Classes) and Views
- input()
- and models updates
plusieurs fichiers controller à écrire : scinder
"""

# Use Factory Method



# player_uuid
# on donne un uuid, il doit renvoyer un Player
# tenir un registre des differents players créés
# doit etre au courant de la création des instances de Player
# methode factory (voir tuto design pattern)

"""
class Thingy(object):
    instances = []

    def __init__(self):
        self.instances.append(self)

def waste_time_and_memory():
    t = Thingy()

for i in range(5):
    waste_time_and_memory()

print Thingy.instances
"""

# pour tournoi
# unicité
# propriete getter qui return : name, location, date_pod
# pour ne pas instancier deux fois player_controller.py
# -> fait dans Class Tournament : identifier


# class PlayerCreator(Creator):  # ???
"""
    Subclass of Creator to create Player instances
    à continuer ...
"""
def create_player(player_dict): # à voir !
    """
    This method creates Player instances
    and hold a registry of the created players.
    à continuer ...
    """
    # return new player instance
    new_player = Player(**player_dict)
    Player.registry[new_player.identifier_pod] = new_player  # registry = {} : key = Player.identifier, value = instance
    return new_player


def get_player_by_id(player_id):  # on entre un uuid et on recupere un player
    """
    This method enables to get a Player instance from its identifier attribute.
    """
    registry = Player.registry
    if player_id in registry:
        return registry[player_id].identifier

    """
    for _obj in gc.get_objects(): # garbage collector : pb lenteur si il y a beaucoup d'instances d'objet de créées
        if isinstance(_obj, Player) and player_id == _obj.identifier_pod:
            return _obj
        # Player # faux
        # player_id = Player.identifier # faux
        # print(player_id) # faux
    """

"""
# Pour sérialiser toutes les instances de joueurs:
self.instances = [] if self.instances is None else self.instances.append(self) (dans la classe Player)

# Pour sauvegarder plusieurs instances de joueurs serialisées dans TinyDB:
db = TinyDB(‘db.json’)
players_table = db.table(‘players’)
players_table.truncate()	# clear the table first
players_table.insert_multiple(serialized_players)

# Pour recharger les joueurs sérialisés, tu peux faire ceci
serialized_players = players_table.all()
"""