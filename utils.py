# coding=utf-8
"""
File for general utils functions
"""

from os import system
from sys import platform


def clear_terminal():
    """
    This function enables to clear the terminal
    """
    if platform.startswith == 'win':
        system('cls')

    else:
        system('clear')
