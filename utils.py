
from os import system
from sys import platform


def clear_terminal():
    if platform.startswith == 'win':
        system('cls')

    else:
        system('clear')

