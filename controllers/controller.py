# coding=utf-8

import sys

from models.models_utils import data
from utils import clear_terminal


class Controller:
    """
    General parent class for all controllers.
    """

    def __init__(self, menu=None):
        self.menu = menu
        self.data = None

    def run(self) -> None:
        """
        This method displays the menu and responds to choices made.
        """
        valid_choices = range(len(self.menu.choices))
        choice = -1
        while choice not in valid_choices:
            self.menu.show()
            _input = input('Enter an option: ')
            clear_terminal()
            try:
                choice = int(_input)
                if choice not in valid_choices:
                    print(f'-> "{choice}" is not a valid choice <-')
            except ValueError:
                print(f'-> "{_input}" is not a valid choice <-')
        clear_terminal()
        action = self.menu.choices[choice]
        action()

    @staticmethod
    def quit() -> None:
        """
        This method quits the program
        """
        sys.exit(0)

    @staticmethod
    def load() -> None:
        """
        This method loads a database file
        """
        data.load()

    @staticmethod
    def save() -> None:
        """
        This method saves data in a database file
        """
        data.save()
