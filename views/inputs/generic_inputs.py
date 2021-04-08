# coding=utf-8

import re
from datetime import date

from constants import ALPHABETICAL_STRING_RULE, ALPHA_NUMERICAL_STRING_RULE


def ask_alphabetical_string(input_info: str) -> str:
    _input = input(input_info)
    while not re.match(ALPHABETICAL_STRING_RULE, _input):
        print('Unauthorized characters found, please retry...')
        _input = input(input_info)
    return _input


def ask_alphanumerical_string(input_info: str) -> str:
    _input = input(input_info)
    while not re.match(ALPHA_NUMERICAL_STRING_RULE, _input):
        print('Unauthorized characters found, please retry...')
        _input = input(input_info)
    return _input


def ask_iso_date(input_info: str) -> date:
    valid_date = False
    _input = input(input_info)
    while not valid_date:
        try:
            _input = date.fromisoformat(_input)
            valid_date = True
        except ValueError:
            print('Not in format YYYY-MM-DD, please retry...')
            _input = input(input_info)
    return _input
