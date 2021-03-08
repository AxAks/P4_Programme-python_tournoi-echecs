# coding=utf-8

import re

"""
This file contains all the constants used in the project.
"""

# Class Player
MINIMUM_AGE = 12
MAXIMUM_RANKING = 3000
MINIMUM_RANKING = 100


# Regex
ALPHABETICAL_STRING_RULE = re.compile("^[A-ZÉÈÇÀa-zéèçà\- ]+$")
ALPHA_NUMERICAL_STRING_RULE = re.compile("^[A-ZÉÈÇÀa-zéèçà0-9_\- ]+$")


# Controller Creator
PLAYER_PROPERTIES = ['last_name', 'identifier', 'first_name', 'birthdate', 'gender', 'ranking']
TOURNAMENT_PROPERTIES = ['name', 'location', 'start_date', 'end_date', 'players_identifier',
                         'time_control', 'description', 'rounds_list', 'rounds']
ROUND_PROPERTIES = ['name', 'matches', 'end_time', 'start_time']
MATCH_PROPERTIES = ['player1_id', 'player2_id', 'player1_score', 'player2_score']