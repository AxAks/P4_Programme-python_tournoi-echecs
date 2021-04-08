# coding=utf-8

from models.models_utils.superfactory import super_factory as sf
from models.models_utils.factory import Factory
from models.player import Player


class PlayerManager(Factory):

    def __init__(self):
        pass

def search_one_player():
    # pas dans la classe ! function et non methode
    # pas générique ! (à scinder entre Models(player_manager qui hérite de Factory?, controllers et views)
    # + voir players_controller : search_by_id
    _input = input('Search a player by id : ')
    results = sf.factories[Player].search(_input)
    while len(results) > 1:
        print(f'Results - '
              f'{len(results)} players returned:')
        for identifier in results:  # print dans les views
            print(
                  f'{results[identifier].last_name},'
                  f' {results[identifier].first_name}:'
                  f' {results[identifier].identifier}\n'
                  f'-> {results[identifier].birthdate},'
                  f' {results[identifier].gender_pod.title()},'
                  f' {results[identifier].ranking}\n')

        results = sf.factories[Player].search(input('Please be more specific: '))
        print('---')
    if len(results) == 1:
        for identifier in results:  # print dans les views
            print('1 Player found in Registry for this ID:')
            print(f'Result:\n'
                  f'{results[identifier].last_name},'
                  f' {results[identifier].first_name}'
                  f' {results[identifier].identifier}\n'
                  f'-> {results[identifier].birthdate},'
                  f' {results[identifier].gender_pod.title()},'
                  f' {results[identifier].ranking}')
    if len(results) == 0:
        print("No Player found in Registry for this ID")
        return results
    else:
        return results


def list_all_players():
    players_list = []
    for uuid in sf.factories[Player].registry:
        player_obj = sf.factories[Player].registry[uuid]
        players_list.append(player_obj)
    return players_list