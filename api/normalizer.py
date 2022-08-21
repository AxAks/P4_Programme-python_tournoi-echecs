import re
from datetime import date, timedelta

from constants import TOURNAMENT_PROPERTIES, PLAYER_PROPERTIES, ALPHABETICAL_STRING_RULE, MINIMUM_AGE, RANKING_RANGE
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
    errors = {}

    for field in request_data:
        if field in needed_properties:

            if field in ['last_name', 'first_name']:
                if not re.match(ALPHABETICAL_STRING_RULE, request_data[field]):
                    errors[field] = f"{field} must only contain alphanumerical characters"
                else:
                    new_player_dict[field] = request_data[field]

            elif field in ['birthdate']:
                try:
                    iso_birthdate = date.fromisoformat(request_data[field])
                except ValueError:
                    errors[field] = f"{field} must be in format YYYY-MM-DD"

                if date.today() - iso_birthdate < timedelta(days=MINIMUM_AGE * 365):
                    errors[field] = "Players must be at least 12 year old"
                else:
                    new_player_dict[field] = iso_birthdate

            elif field in ['gender']:
                if request_data[field] not in ['MALE', 'FEMALE']:
                    errors[field] = "Gender must be 'MALE' or 'FEMALE'"
                else:
                    new_player_dict[field] = request_data[field]

            elif field in ['ranking']:
                try:
                    ranking_as_int = int(request_data[field])
                except ValueError:
                    errors[field] = f"{field} must be a digit between 100 and 3000"

                if ranking_as_int in RANKING_RANGE:
                    new_player_dict[field] = ranking_as_int
                else:
                    errors[field] = f"{field} must be a digit between 100 and 3000"

    if errors:
        return errors
    else:
        new_player = sm.managers[Player].create(**new_player_dict)
        return new_player


def tournament_normalizer():
    pass
    TOURNAMENT_PROPERTIES