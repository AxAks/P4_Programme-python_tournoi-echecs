# coding=utf-8

import re

"""
This file contains the project-wide constants.
"""

# Class Player
MINIMUM_AGE = 12
MAXIMUM_RANKING = 3000
MINIMUM_RANKING = 100
RANKING_RANGE = range(100, 3001)

# Regex
ALPHABETICAL_STRING_RULE = re.compile("^[A-ZÉÈÇÀa-zéèçà\- ']+$")
ALPHA_NUMERICAL_STRING_RULE = re.compile("^[A-ZÉÈÇÀa-zéèçà0-9_\- ]+$")

# Factory
EMPTY_SEARCH_STRINGS = ['', ' ', '-', '_', '.', '()']

TOURNAMENT_PROPERTIES = ['name', 'location', 'start_date', 'end_date', 'identifiers_list',
                         'time_control', 'description', 'rounds_list', 'rounds']

PLAYER_PROPERTIES = ['last_name', 'identifier', 'first_name', 'birthdate', 'gender', 'ranking']
ROUND_PROPERTIES = ['name', 'matches', 'end_time', 'start_time']
MATCH_PROPERTIES = ['player1_id', 'player2_id', 'player1_score', 'player2_score']
