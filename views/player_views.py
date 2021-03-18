# coding=utf-8


"""
temp : just for me !!
Views = Interface computer/ user

- input()  # car logique d'interchageabilité, toutes les fonctions d'interface entrée/sortie au meme endroit
- print()
- messages

plusieurs fichiers view à écrire : scinder
"""
import sys

from controllers.creator import Creator
from controllers.player_controller import PlayerCreator
from models.player import Player

class PlayerMenu:
    """
    This class manages a menu to navigate through the Player Database Management.
    """

    def __init__(self):
        self.choices = {
            '1': self.add_player,
            '2': self.search_player,
            '3': self.edit_player,
            '4': self.save_tournament,
            '5': self.load_tournament,
            '0': self.quit
        }

    def player_menu(self):
        """
        This method displays the different options of the menu: Player Database.
        """
        print('Chess Tournament Manager\n'
              '-Players Menu-\n'
              '\n1. Add New Player\n'
              '2. Search Players\n'
              '3. Edit Players\n'
              '4. Load State\n'
              '5. Save State\n'
              '\n0. Quit')

    def run(self):
        """
        This method displays the menu and responds to choices made.
        """
        while True:
            self.player_menu()
            choice = input('\nEnter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'"{choice}" is not a valid choice')

    def add_player(self):
        pass

    def search_player(self):
        pass

    def edit_player(self):
        pass

    def save_tournament(self):  # Doublon General menu, doit etre factorisé car doit accessible de partout: "sauver l'etat du systeme"
        pass

    def load_tournament(self):  # Doublon general menu
        pass

    def quit(self):  # Doublon general menu
        print('Chess Tournament Manager terminated')
        sys.exit(0)
