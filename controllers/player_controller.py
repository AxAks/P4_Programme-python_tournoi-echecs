# coding=utf-8

from models.player import Player

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
# methode factory (voir tuto design pattern)
# class PlayerCreator:  # est ce que je mets tout ca dans une classe (cf Factory Method)???
"""
Subclass of the Class Creator to create Player instances
à continuer ...
"""

# doit etre au courant de la création des instances de Player
# tenir un registre des differents players créés
def create_player(player_dict):  #  à voir !
    """
    This method creates Player instances
    and hold a registry of the created players.
    à continuer ...
    """
    new_player = Player(**player_dict)
    Player.registry[
        new_player.identifier_pod] = new_player  # registry = {} : key = Player.identifier, value = instance
    return new_player
"""
# return new player instance
new_player = Player(**player_dict)
Player.registry[new_player.identifier_pod] = new_player  # registry = {} : key = Player.identifier, value = instance
return new_player
"""

# on donne un player_uuid, il doit renvoyer un Player
def get_player_by_id(player_id):
    """
    This method enables to get a Player instance from its identifier attribute.
    """
    registry = Player.registry
    if player_id in registry:
        return registry[player_id]

    """
    for _obj in gc.get_objects(): # garbage collector : pb lenteur si il y a beaucoup d'instances d'objet de créées
        if isinstance(_obj, Player) and player_id == _obj.identifier_pod:
            return _obj
        # Player # faux
        # player_id = Player.identifier # faux
        # print(player_id) # faux
    """

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