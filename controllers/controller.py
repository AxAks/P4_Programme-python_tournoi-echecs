# coding=utf-8
import sys

from models.models_utils import data


class Controller:
    def __init__(self, menu=None):
        self.menu = menu

    def run(self) -> None:
        """
        This method displays the menu and responds to choices made.
        """
        valid_choices = range(len(self.menu.choices))
        choice = -1
        while choice not in valid_choices:
            self.menu.show()
            _input = input('Enter an option: ')
            try:
                choice = int(_input)
                if choice not in valid_choices:
                    print(f'-> "{choice}" is not a valid choice <-')
            except ValueError:
                print(f'-> "{_input}" is not a valid choice <-')

        action = self.menu.choices[choice]
        action()

    def quit(self):
        sys.exit(0)

    def load(self):
        data.load()

    def save(self):
        data.save()
