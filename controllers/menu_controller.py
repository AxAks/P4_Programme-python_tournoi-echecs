# coding=utf-8
"""
manage menus via controllers
"""
import sys

from tinydb import TinyDB

from models.player import Player
from models.superfactory import super_factory as sf
from models.tournament import Tournament

from views.forms.new_tournament_form import NewTournamentForm
from views.menus.player_menu import PlayerMenu
from views.menus.tournament_menu import TournamentMenu
from views.menus.home_menu import HomeMenu
from views.forms.new_player_form import NewPlayerForm
from views.menus.list_players_menu import ListPlayerMenu
from views.menus.list_tournaments_menu import ListTournamentsMenu


# passer par le controller pour afficher les menus
# enlever l'intelligence de Menu et la passer dans controller
# pb mon intelligence pour les menu est dans Menu et le systeme est hérité dans les menus specifique
# debut avec home_menu et ensuite calquer

# on fait juste des endpoints dans le controller pour la navigation.
# on laisse un peu'intelligence dans les views Menu et Form
# quand on manipule Modeles et Views, on met dans le controller.


#Pour recharger les joueurs sérialisés, tu peux faire ceci :

# serialized_players = players_table.all()
# serialized_tournaments = tournaments_table.all()


  # pb chemin de la DB JSon, je la mets où (dans le code et dans le projet ?), le mieux est à la base du projet


db = TinyDB('db.json', ensure_ascii=False)
db_test = TinyDB('db_test.json', ensure_ascii=False)


# Fonctions générales
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
    print(f'Program state loaded via "db.json"(funct to write)')  # passer le print dans Menu().load() quand fonction ecrite


def save():  # à continuer, bien tester et checker si erreurs et si on peut choisir le nom du fichier sauvegardé
    """
    This function saves the program state using tinyDB.
    It serializes the instances of Player et Tournament
    and create a db.json file to store them as dicts
    """
    serialized_player_instances = \
        [sf.factories[Player].registry[key].serialize() for key in sf.factories[Player].registry]
    serialized_tournament_instances = \
        [sf.factories[Tournament].registry[key].serialize() for key in sf.factories[Tournament].registry]
    players_table = db_test.table('players')
    tournaments_table = db_test.table('tournaments')
    players_table.truncate()
    tournaments_table.truncate()
    players_table.insert_multiple(serialized_player_instances)
    tournaments_table.insert_multiple(serialized_tournament_instances)


def quit():
    """
    This function exits the program
    """
    sys.exit(0)


# redirections menu

def to_home_menu():
    """
    This function redirects to the Home menu
    """
    HomeMenu().run()


def to_player_menu():
    """
    This function redirects to the Players Database Manager menu
    """
    PlayerMenu().run()


def to_new_player_form():
    """
    This function redirects to the Player Creation Form
    """
    NewPlayerForm().run()


def to_list_all_players():
    """
    This function redirects to the Menu used to
    display sorted or filtered lists of Players from the Database.
    """
    ListPlayerMenu().run()


def to_tournament_menu():
    """
    This function redirects to the Tournaments Manager menu
    """
    TournamentMenu().run()


def to_list_all_tournaments():
    """
    This function redirects to the Menu used to
    display sorted or filtered lists of Tournaments from the Database.
    """
    ListTournamentsMenu().run()


def to_new_tournament_form():
    """
    This function redirects to the Tournament Creation Form
    """
    NewTournamentForm().run()
