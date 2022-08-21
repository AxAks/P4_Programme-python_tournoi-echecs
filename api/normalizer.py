
from constants import TOURNAMENT_PROPERTIES, PLAYER_PROPERTIES
from models.models_utils import data
from models.models_utils.supermanager import super_manager as sm
from models.player import Player

"""
TOURNAMENT_PROPERTIES = ['name', 'location', 'start_date', 'end_date', 'rounds', 'time_control', 'description',
                         'identifiers_list', 'rounds_list', 'total_results', 'not_played_yet', 'done']

PLAYER_PROPERTIES = ['last_name', 'identifier', 'first_name', 'birthdate', 'gender', 'ranking']
"""


def player_normalizer(request_data):
    not_asked_properties = ['identifier']
    needed_properties = PLAYER_PROPERTIES.copy()
    for _property in needed_properties:
        if _property in not_asked_properties:
            needed_properties.remove(_property)

    new_player_dict = {}

    for field in request_data:
        if field in needed_properties:
            if field == 'ranking':
                new_player_dict[field] = int(request_data[field])
            else:
                new_player_dict[field] = request_data[field]
    print(new_player_dict)
    print(f" Type ranking: {type(new_player_dict['ranking'])} - {new_player_dict['ranking']}")
    new_player = sm.managers[Player].create(**new_player_dict)
    data.save()
    return new_player


def tournament_normalizer():
    pass
    TOURNAMENT_PROPERTIES