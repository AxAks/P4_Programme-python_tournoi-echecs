# coding=utf-8
from typing import Union

from models.models_utils.superfactory import super_factory as sf
from models.models_utils.factory import Factory
from models.player import Player


class PlayerManager(Factory):

    def __init__(self):
        pass


def search_one_player() -> Union[dict[Player], Player]:
    # pas dans la classe ! function et non methode
    # pas générique ! (à scinder entre Models(player_manager qui hérite de Factory?, controllers et views)
    # + voir players_controller : search_by_id
    _input = input('Search a player by id : ')
    results = sf.factories[Player].search(_input)
    while len(results) > 1:
        print(f'Results - '
              f'{len(results)} players returned:')  # print dans les views
        for identifier in results:
            print(
                  f'{results[identifier].last_name},'
                  f' {results[identifier].first_name}:'
                  f' {results[identifier].identifier}\n'
                  f'-> {results[identifier].birthdate},'
                  f' {results[identifier].gender_pod.title()},'
                  f' {results[identifier].ranking}\n')

        results = sf.factories[Player].search(input('Please be more specific: '))
        print('---')
    if len(results) == 1:  # print dans les views
        for identifier in results:
            print('1 Player found in Registry for this ID:')
            print(f'Result:\n'
                  f'{results[identifier].last_name},'
                  f' {results[identifier].first_name}'
                  f' {results[identifier].identifier}\n'
                  f'-> {results[identifier].birthdate},'
                  f' {results[identifier].gender_pod.title()},'
                  f' {results[identifier].ranking}')
            player_obj = results[identifier]
            return player_obj
    if len(results) == 0:
        print("No Player found in Registry for this ID")
        return results


def list_registered_players() -> list[Player]:
    players_list = []
    for uuid in sf.factories[Player].registry:
        player_obj = sf.factories[Player].registry[uuid]
        players_list.append(player_obj)
    return players_list