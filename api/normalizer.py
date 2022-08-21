import re
from datetime import date, timedelta
from typing import List
from uuid import UUID

from constants import TOURNAMENT_PROPERTIES, PLAYER_PROPERTIES, ALPHABETICAL_STRING_RULE, MINIMUM_AGE, RANKING_RANGE, \
    ALPHA_NUMERICAL_STRING_RULE
from models.models_utils.player_manager import PlayerManager
from models.models_utils.supermanager import super_manager as sm
from models.player import Player
from models.tournament import Tournament

"""
TOURNAMENT_PROPERTIES = ['name', 'location', 'start_date', 'end_date', 'rounds', 'time_control', 'description',
                         'identifiers_list', 'rounds_list', 'total_results', 'not_played_yet', 'done']

PLAYER_PROPERTIES = ['last_name', 'identifier', 'first_name', 'birthdate', 'gender', 'ranking']
"""


def player_normalizer(request_data):
    not_asked_properties = ['identifier']
    needed_properties = PLAYER_PROPERTIES.copy()
    for _property in PLAYER_PROPERTIES:
        if _property in not_asked_properties:
            needed_properties.remove(_property)

    new_player_dict = {}
    errors = {}

    for field in request_data:
        if field in needed_properties:

            if field in ['last_name', 'first_name']:
                if not re.match(ALPHABETICAL_STRING_RULE, request_data[field]):
                    errors[field] = f"{field} must only contain alphabetical characters"
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


def tournament_normalizer(request_data):
    not_asked_properties = ['rounds_list', 'total_results', 'not_played_yet', 'done']
    needed_properties = TOURNAMENT_PROPERTIES.copy()
    for _property in TOURNAMENT_PROPERTIES:
        if _property in not_asked_properties:
            needed_properties.remove(_property)

    new_tournament_dict = {}
    errors = {}

    for field in request_data:
        if field in needed_properties:

            if field in ['name']:
                if not re.match(ALPHA_NUMERICAL_STRING_RULE, request_data[field]):
                    errors[field] = f"{field} must only contain alphanumerical characters"
                else:
                    new_tournament_dict[field] = request_data[field]

            elif field in ['location']:
                if not re.match(ALPHABETICAL_STRING_RULE, request_data[field]):
                    errors[field] = f"{field} must only contain alphabetical characters"
                else:
                    new_tournament_dict[field] = request_data[field]

            elif field in ['start_date', 'end_date']:
                try:
                    iso_date = date.fromisoformat(request_data[field])
                except ValueError:
                    errors[field] = f"{field} must be in format YYYY-MM-DD"

                if (field == 'start_date') and ('end_date' in request_data.keys()):
                    if iso_date > date.fromisoformat(request_data['end_date']):
                        errors[field] = f"End Date cannot be prior to Start Date"
                    else:
                        new_tournament_dict[field] = request_data[field]
                elif (field == 'end_date') and ('start_date' in request_data.keys()):
                    if iso_date < date.fromisoformat(request_data['start_date']):
                        errors[field] = f"End Date cannot be prior to Start Date"
                    else:
                        new_tournament_dict[field] = request_data[field]

            elif field in ['rounds']:
                try:
                    rounds_as_int = int(request_data[field])
                    new_tournament_dict[field] = rounds_as_int
                except ValueError:
                    errors[field] = f"{field} must be a number"

            elif field in ['time_control']:
                if request_data[field] not in ['BULLET', 'BLITZ', 'RAPIDE']:
                    errors[field] = f"{field} must be 'BULLET', 'BLITZ' or 'RAPIDE'"
                else:
                    new_tournament_dict[field] = request_data[field]

            elif field in ['description']:
                if request_data[field] == '':
                    errors[field] = f"{field} cannot be empty"
                else:
                    new_tournament_dict[field] = request_data[field]

            elif field in ['identifiers_list']:
                split_list_of_players = request_data[field].split(',')
                # trick because as string in postman (input must be a list)
                if (not isinstance(split_list_of_players, List)) \
                        or (len(split_list_of_players) < 4) \
                        or (len(split_list_of_players) % 2 != 0):
                    errors[f"{field}_list_error"] = f"{field} must be a even list of minimum 4 players identifiers"

                available_players = len(PlayerManager().registry)
                if available_players < len(split_list_of_players):
                    errors[f"{field}_insufficient_players"] = \
                        f"Not enough players in the registry, Please create more players first"

                not_registered_players = []
                for identifier in split_list_of_players:
                    if UUID(identifier) not in PlayerManager().registry.keys():
                        not_registered_players.append(identifier)

                if not_registered_players:
                    errors[f"{field}_not_found_players"] = \
                        f"The following identifiers could not be found in the registry: {not_registered_players}"

                if len(split_list_of_players) > len(set(split_list_of_players)):
                    errors[f"{field}_duplicate_player"] = f"Player Identifiers in the list must be unique"

                new_tournament_dict[field] = split_list_of_players

    if errors:
        return errors
    else:
        new_tournament = sm.managers[Tournament].create(**new_tournament_dict)
        return new_tournament
