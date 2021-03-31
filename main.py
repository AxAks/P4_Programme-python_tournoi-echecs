# coding=utf-8

"""
File to launch the program:
from the terminal : python main.py
the file is located at the root of the project,
it redirects to the Home Menu file in the views directory.
"""
from models.models_utils import load
from models.models_utils.superfactory import super_factory as sf
from models.player import Player
from models.tournament import Tournament
from controllers.home_controller import HomeCtrl


def main():
    """
    This function launches the program
    It creates the Factories for Player and Tournament
    loads the registries form the database file
    and then directs to the Home menu
    """
    sf.create_factory(Player)
    sf.create_factory(Tournament)
    load.load()
    HomeCtrl().run()


if __name__ == '__main__':
    main()
