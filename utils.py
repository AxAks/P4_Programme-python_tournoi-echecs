
from os import system
from sys import platform


def clear_terminal():
    if platform.startswith == 'win':
        system('cls')

    else:
        system('clear')


# ajouter la possibilité de cancel, retour au menu precedent, en restant générique ...
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
