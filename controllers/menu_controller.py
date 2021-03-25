# coding=utf-8
"""
manage menus
"""

# passer par le controller pour afficher les menus
# enlever l'intelligence de Menu et la passer dans controller
# pb mon intelligence pour les menu est dans Menu et le systeme est hérité dans les menus specifique
# debut avec home_menu et ensuite calquer
from views.menus.menu import Menu

from views.menus.player_menu import PlayerMenu
from views.menus.tournament_menu import TournamentMenu
from views.menus.home_menu import HomeMenu

def to_player_menu():
    PlayerMenu().run()


def to_tournament_menu():
    TournamentMenu().run()


def to_home_menu():
    HomeMenu().run()


