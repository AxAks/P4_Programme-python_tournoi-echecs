# coding=utf-8
from models.models_utils.factory import Factory
from models.player import Player
from models.models_utils.superfactory import super_factory as sf
from views.forms.add_player_form import NewPlayerForm
from views.menus.player_menu import PlayerMenu

"""
Controller file for Player
"""


def run():
    """
    This method displays the menu and responds to choices made.
    """
    valid_choices = range(len(PlayerMenu().choices))
    choice = -1
    while choice not in valid_choices:
        PlayerMenu().show()
        _input = input('Enter an option: ')
        try:
            choice = int(_input)
            if choice not in valid_choices:
                print(f'-> "{choice}" is not a valid choice <-')
        except ValueError:
            print(f'-> "{_input}" is not a valid choice <-')

    action = PlayerMenu().choices[choice]
    action()


def add_player():
    new_player_dict = NewPlayerForm().add_new_player()
    new_player = Factory(Player).create(**new_player_dict)
    return new_player

def sort_by_last_name():
    players_list = []
    for uuid in sf.factories[Player].registry:
        player_obj = sf.factories[Player].registry[uuid]
        players_list.append(player_obj)
    sorted_by_last_name = sorted(players_list, key=lambda x: x.last_name)
    return sorted_by_last_name


def sort_by_ranking():
    players_list = []
    for uuid in sf.factories[Player].registry:
        player_obj = sf.factories[Player].registry[uuid]
        players_list.append(player_obj)
    sorted_by_ranking = sorted(players_list, key=lambda x: x.ranking, reverse=True)
    return sorted_by_ranking


def search_by_id(search):
    """
    This function lists the player instances matching the given input (id)
    """
    results = sf.factories[Player].search(search)
    found_players_list = []
    for uuid in results:
        player_obj = sf.factories[Player].registry[uuid]
        found_players_list.append(player_obj)
    return found_players_list




