# coding=utf-8
from tinydb import TinyDB

from models.models_utils.superfactory import super_factory as sf
from models.player import Player
from models.tournament import Tournament


db = TinyDB('db.json', ensure_ascii=False)

def save() -> None:  # à continuer, bien tester et checker si erreurs et si on peut choisir le nom du fichier sauvegardé
    """
    This function saves the state of the program state using tinyDB.
    It serializes the instances of Player et Tournament
    and create a db.json file to store them as dicts
    """
    print(f'Saving current program state')
    serialized_player_instances = \
        [sf.factories[Player].registry[key].serialize() for key in sf.factories[Player].registry]
    serialized_tournament_instances = \
        [sf.factories[Tournament].registry[key].serialize() for key in sf.factories[Tournament].registry]
    players_table = db.table('players')
    tournaments_table = db.table('tournaments')
    players_table.truncate()
    tournaments_table.truncate()
    players_table.insert_multiple(serialized_player_instances)
    tournaments_table.insert_multiple(serialized_tournament_instances)
    print('Program state saved')


def load():  # à continuer, bien tester et checker si erreurs et si on peut choisir le fichier à loader
    """
    This method loads dicts for players and tournaments previously saved state of the program
    through a json file database using tinyDB.
    It then deserializes the dicts to get python objects instances
    """
    players_table = db.table('players')
    tournaments_table = db.table('tournaments')
    serialized_players = players_table.all()
    [sf.factories[Player].create(**serialized_player) for serialized_player in serialized_players]
    serialized_tournaments = tournaments_table.all()
    [sf.factories[Tournament].create(**serialized_tournament) for serialized_tournament in serialized_tournaments]
    print(f'Program state loaded from file')
