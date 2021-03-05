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
ALPHA_NUMERICAL_STRING_RULE = re.compile("^[A-ZÉÈÇÀa-zéèçà1-9_\- ]+$")