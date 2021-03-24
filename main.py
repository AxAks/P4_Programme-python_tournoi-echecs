# coding=utf-8

"""
File to launch the program:
from the terminal : python main.py
the file is located at the root of the project,
it redirects to the Home Menu file in the views directory.
"""

from views.menus.home_menu import HomeMenu

from models.superfactory import super_factory as sf
from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round
from tests import sample_values as test_sample

def main():
    player_factory = sf.create_factory(Player)
    tournament_factory = sf.create_factory(Tournament)
    round_factory = sf.create_factory(Round)
    match_factory = sf.create_factory(Match)
    ## simuler la fonction load : remplir les factories avec des boucles for similaires aux tests (au démarrage de l'application on charge l'état)
    # instanciation Players via factory
    [player_factory.create(**player_dict) for player_dict in test_sample.players_list]
    # instanciation Tournaments via factory
    [tournament_factory.create(**tournament_dict) for tournament_dict in test_sample.tournaments_list]
    HomeMenu().run()
    [round_factory.create(**round_dict) for round_dict in test_sample.rounds_list]
    # instanciation Tournaments via factory
    [match_factory.create(**match_dict) for match_dict in test_sample.matchs_list]
    # instanciation Tournaments via factory

    # simuler la fonction save : remplir les factories avec des boucles for similaires aux tests


if __name__ == '__main__':
    main()
