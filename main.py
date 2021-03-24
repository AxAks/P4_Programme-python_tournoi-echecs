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
from tests import sample_values as test_sample


def main():
    # mise en place des factories au démarrage
    player_factory = sf.create_factory(Player)
    tournament_factory = sf.create_factory(Tournament)

    # load_state() , à partir d'un fichier normalement ! test sample // fichier formaté db.json

    ## simuler la fonction load : remplir les factories avec des boucles for similaires aux tests (au démarrage de l'application on charge l'état)
    # instanciation des objets via factory (rounds dans tournoi, matches dans dans round (et player ?)
    [player_factory.create(**player_dict) for player_dict in test_sample.players_list]
    [tournament_factory.create(**tournament_dict) for tournament_dict in test_sample.tournaments_list]  # ca instancie les rounds et les matchs qui vivent dans Tournament

    # tests/verifs
    p = 0
    for player in player_factory.registry:
        p += 1
    t = 0
    for tournament in tournament_factory.registry:
        t += 1
    print(f"---\n"
          f"-> {p} players imported\n"
          f"-> {t} tournaments imported\n"
          f"---")

    # ouverture du menu
    HomeMenu().run()

    # simuler la fonction save : on serialize tout avec des boucles for similaires aux tests
    serialized_player_instances = [player_factory.registry[key].serialize() for key in player_factory.registry]
    [print(serialized_player_instance) for serialized_player_instance in serialized_player_instances]
    print(serialized_player_instances)
    serialized_tournament_instances = [tournament_factory.registry[key].serialize() for key in
                                       tournament_factory.registry]
    [print(serialized_tournament_instance) for serialized_tournament_instance in serialized_tournament_instances]


if __name__ == '__main__':
    main()
