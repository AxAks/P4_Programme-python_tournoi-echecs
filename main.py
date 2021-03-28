# coding=utf-8

"""
File to launch the program:
from the terminal : python main.py
the file is located at the root of the project,
it redirects to the Home Menu file in the views directory.
"""

from models.superfactory import super_factory as sf
from models.player import Player
from models.tournament import Tournament
from controllers import menu_controller


def main():
    """
    This function launches the program
    It creates the Factories for Player and Tournament
    and then directs to the Home menu
    """
    sf.create_factory(Player)
    sf.create_factory(Tournament)
    menu_controller.to_home_menu()


if __name__ == '__main__':
    main()
