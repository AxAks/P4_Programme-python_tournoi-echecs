
from os import system
from sys import platform
from typing import Union


def clear_terminal():
    if platform.startswith == 'win':
        system('cls')

    else:
        system('clear')


# ajouter la possibilité de cancel via form qui herite de views, retour au menu precedent, en restant générique ...
def validate_input(value, method):
    valid_entry = False
    choices_info = '1: YES, 2: NO'
    input_info = f'Please confirm this entry? ({choices_info}): '
    valid_choices = (1, 2)
    wrong_input = 'Invalid choice (1 or 2), please retry...'
    while not valid_entry:
        try:
            _input = input(input_info)
            _input = int(_input)
            if _input in valid_choices:
                if _input == 2:
                    value = method()
                else:
                    valid_entry = True
            else:
                print(wrong_input)
        except ValueError:
            print(wrong_input)
    return value


def lists_to_tuples_list(list1, list2) -> Union[list[tuple], str]:
    """
    This function compares two lists
    and associates their items though their indices in respective list
    """
    if len(list1) == len(list2):
        return [(list1[i], list2[i]) for i in range(0, len(list1))]
    else:
        return 'These lists do not have the same number of items'


def split_even_list(_list) -> Union[tuple[list], str]:
    """
    This function splits a list in the middle into two sub-lists
    """
    if len(_list) % 2 == 0:
        middle_index = len(_list) // 2
        sublist1 = _list[middle_index:]
        sublist2 = _list[:middle_index]
        return sublist1, sublist2
    else:
        return 'This list does not have an even number of items'