# coding=utf-8
"""
manage menus via controllers
"""
import sys

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


# redirections menu

def to_home_menu():
    """
    This function redirects to the Home menu
    """
    HomeMenu().run()


def load():
    print(f'Program state loaded via "database_file"(funct to write)')


def save():
    print('Program state saved(funct to write)')


def quit():
    sys.exit(0)


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

