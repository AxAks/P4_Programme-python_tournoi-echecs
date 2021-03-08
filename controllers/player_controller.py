# coding=utf-8

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
class PlayerController:  # ???

    def create_player(self): # à voir !
        """
        This method hold a registery of the created players.
        """
        pass

    def get_player_by_id(self, player_id):  # ??? à voir !
        """
        This method enables to get a Player instance from its identifier attribute.
        """
        Player # faux
        player_id = Player.identifier # faux
        print(player_id) # faux


# on entre un uuid et on recupere un player


# registre : dict !!!!
# key : uuid
# value : instance


# unicité
# pour tournoi
# propriete getter qui return : name, location, date_pod
# pour ne pas instancier deux fois player_controller.py

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