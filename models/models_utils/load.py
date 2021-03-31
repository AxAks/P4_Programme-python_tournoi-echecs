# coding=utf-8

from tinydb import TinyDB

from models.models_utils.superfactory import super_factory as sf
from models.player import Player
from models.tournament import Tournament


db = TinyDB('db.json', ensure_ascii=False)


def load() -> None:
    """
    This method directs to the controller
    to load a previously saved state of the program from a database file at any time.
    """
    load.load()
    print(f'Program state loaded from file')


def load():  # à continuer, bien tester et checker si erreurs et si on peut choisir le fichier à loader
    """
    This method loads dicts for players and tournaments from a json file database using tinyDB.
    It then deserializes the dicts to get python objects instances
    """
    players_table = db.table('players')
    tournaments_table = db.table('tournaments')
    serialized_players = players_table.all()
    [sf.factories[Player].create(**serialized_player) for serialized_player in serialized_players]
    serialized_tournaments = tournaments_table.all()
    [sf.factories[Tournament].create(**serialized_tournament) for serialized_tournament in serialized_tournaments]