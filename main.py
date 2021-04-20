# coding=utf-8

"""
File to launch the program:
from the terminal : python main.py
the file is located at the root of the project,
it redirects to the Home Menu file in the views directory.
"""

from models.models_utils import data
from models.models_utils.supermanager import super_manager as sm
from models.player import Player
from models.tournament import Tournament
from controllers.home_controller import HomeCtrl
from utils import clear_terminal


def main():
    """
    This function launches the program
    It creates the Factories for Player and Tournament
    loads the registries from the database file
    and then directs to the Home menu
    """
    clear_terminal()
    sm.create_manager(Player)
    sm.create_manager(Tournament)
    data.load()
    HomeCtrl().run()


if __name__ == '__main__':
    main()
