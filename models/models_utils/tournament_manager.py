# coding=utf-8

from models.models_utils.superfactory import super_factory as sf
from models.models_utils.factory import Factory
from models.tournament import Tournament


class TournamentManager(Factory):

    def __init__(self):
        pass

    def search_one_tournament(self) -> list[Tournament]:
        # pas dans la classe, function et non methode
        # pas générique ! (à scinder entre Models(tournament_manager qui hérite de Factory?, controllers et views),pas testé
        # + voir list tournament controller : search_by_id
        _input = input('Search a tournament by name, location or dates: ')
        results = sf.factories[Tournament].search(_input)
        while len(results) > 1:
            print(f'Results - '
                  f'{len(results)} Tournaments returned:')
            for identifier in results:
                print(f'{results[identifier].name}, '  # les prints sont dans les views !!!
                      f' {results[identifier].location}, '
                      f' {results[identifier].start_date}, '
                      f' {results[identifier].end_date}\n'
                      f'-> {results[identifier].description}')

            results = sf.factories[Tournament].search(input('please be more specific: '))
            print('---')
        if len(results) == 1:
            for identifier in results:
                print('1 Tournament found in Registry for this research:')  # les prints sont dans les views !!!
                print(f'Result:\n'
                      f'{results[identifier].name}, '
                      f' {results[identifier].location}, '
                      f' {results[identifier].start_date}, '
                      f' {results[identifier].end_date}\n'
                      f'-> {results[identifier].description}')
        if len(results) == 0:
            print("No Tournament found in Registry for this research")
            return results
        else:
            return results

    def list_registered_tournaments(self) -> list[Tournament]:
        tournaments_list = []
        for identifier in sf.factories[Tournament].registry:
            tournament_obj = sf.factories[Tournament].registry[identifier]
            tournaments_list.append(tournament_obj)
        return tournaments_list