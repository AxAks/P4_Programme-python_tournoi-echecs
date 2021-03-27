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


db = TinyDB('db.json', ensure_ascii=False) # pb chemin de la DB JSon, je la mets où (dans le code et dans le projet ?)

# Fonctions générales

def load():
    print(f'Program state loaded via "database_file"(funct to write)')  # passer le print dans Menu().load() quand fonction ecrite


def save():
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


def quit():
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
