# coding=utf-8
from tinydb import TinyDB

from models.models_utils.supermanager import super_manager as sm
from models.player import Player
from models.tournament import Tournament


db = TinyDB('db.json', ensure_ascii=False)


def save() -> None:
    """
    This function saves the state of the program state using tinyDB.
    It serializes the instances of Player et Tournament
    and create a db.json file to store them as dicts
    """
    print('Saving current program state')
    serialized_player_instances = \
        [sm.managers[Player].registry[key].serialize() for key in sm.managers[Player].registry]
    serialized_tournament_instances = \
        [sm.managers[Tournament].registry[key].serialize() for key in sm.managers[Tournament].registry]
    players_table = db.table('players')
    tournaments_table = db.table('tournaments')
    players_table.truncate()
    tournaments_table.truncate()
    players_table.insert_multiple(serialized_player_instances)
    tournaments_table.insert_multiple(serialized_tournament_instances)
    print('Program state saved')


def load() -> None:
    """
    This method loads dicts for players and tournaments previously saved state of the program
    through a json file database using tinyDB.
    It then deserializes the dicts to get python objects instances
    """
    players_table = db.table('players')
    tournaments_table = db.table('tournaments')
    serialized_players = players_table.all()
    [sm.managers[Player].create(**serialized_player) for serialized_player in serialized_players]
    serialized_tournaments = tournaments_table.all()
    [sm.managers[Tournament].create(**serialized_tournament) for serialized_tournament in serialized_tournaments]
    print('Program state loaded from file')
