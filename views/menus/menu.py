# coding=utf-8

"""
Generic Class for Menu
"""

import sys


class Menu:
    """
    This class is a parent Class for all Menu screens
    It enables to navigate through the program.
    """
    def __init__(self):
        self.menu_name = 'Menu'
        self.choices = [self.back, self.save_state, self.load_state]

    def menu(self) -> None:
        """
        This method displays the different options of the menu.
        """
        for choice in self.choices:
            reformated_choice_str = choice.__name__.replace('_', ' ').title()
            print(f"{self.choices.index(choice)}: {reformated_choice_str}")

    def run(self) -> None:
        """
        This method displays the menu and responds to choices made.
        """
        print(self.menu_name)
        while True:
            valid_choices = range(len(self.choices))
            choice = -1
            while choice not in valid_choices:
                self.menu()
                _input = input('\nEnter an option: ')
                try:
                    choice = int(_input)
                    if choice not in valid_choices:
                        print(f'-> "{choice}" is not a valid choice <-')
                except ValueError:
                    print(f'-> "{_input}" is not a valid choice <-')

            action = self.choices[choice]
            action()

    def back(self) -> None:
        """
        This method enables to go back to the previous screen
        The program quits if the screen is the root menu.
        """
        if "currentMenu".run() == "HomeMenu".run():  # pseudo-code à definir
            print('Program terminated')
            sys.exit(0)
        else:
            print('Back to previous Menu Screen')
            "PreviousSpecificMenu()".run()  # pseudo-code à definir

    def save_state(self) -> None:  # on enregistrera dans TinyDB apres serialisation de tous les Players et Tournaments (via les registres)
        """
        This method enables to save the state of the program at any time.
        """
        print('Program state saved')

    def load_state(self, database_file) -> None:  # on chargera depuis TinyDB : deserialisation de tous les Players et Tournaments (instanciation via creators)
        """
        This method enables to load a previously saved state of the program from a database file at any time.
        """
        print(f'Program state loaded via {database_file}')
