# coding=utf-8
from typing import Union

from models.models_utils.superfactory import super_factory as sf
from models.models_utils.factory import Factory
from models.tournament import Tournament


class TournamentManager(Factory):

    def __init__(self):
        pass

    def search_one_tournament(self) -> Union[dict[Tournament], Tournament]:  # A revoir réécrire !!
        # pas générique ! (à scinder entre Models(tournament_manager qui hérite de Factory?, controllers et views),pas testé
        # + voir list tournament controller : search_by_id
        print('========================')
        _input = input('Search a tournament by name, location or dates: ')
        results = sf.factories[Tournament].search(_input)
        while len(results) > 1:
            print(f'{len(results)} Tournaments returned:')
            for identifier in results:
                tournament_obj = results[identifier]
                print(f'{tournament_obj.name}, '  #  les prints sont dans les views !!!
                      f' {tournament_obj.location}, '
                      f' {tournament_obj.start_date}, '
                      f' {tournament_obj.end_date}\n'
                      f'-> {tournament_obj.description}')
            results = sf.factories[Tournament].search(input(f'Please be more specific: '))
            print('---')
        if len(results) == 1:
            for identifier in results:
                tournament_obj = results[identifier]
                return tournament_obj
        if len(results) == 0:

            return results

    def list_registered_tournaments(self) -> list[Tournament]:
        tournaments_list = []
        for identifier in sf.factories[Tournament].registry:
            tournament_obj = self.from_identifier_to_tournament_obj(identifier)
            tournaments_list.append(tournament_obj)
        return tournaments_list

    def from_identifier_to_tournament_obj(self, identifier):
        player_obj = sf.factories[Tournament].registry[identifier]
        return player_obj
