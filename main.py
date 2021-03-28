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

from tests import sample_values as test_sample  # à supprimer plus tard


def main():
    player_factory = sf.create_factory(Player)
    tournament_factory = sf.create_factory(Tournament)

    # à mettre dans la fonction load()
    [player_factory.create(**player_dict) for player_dict in test_sample.players_list]
    [tournament_factory.create(**tournament_dict) for tournament_dict in test_sample.tournaments_list]  # ca instancie les rounds et les matchs qui vivent dans Tournament

    # lancement du menu
    menu_controller.to_home_menu()

if __name__ == '__main__':
    main()
