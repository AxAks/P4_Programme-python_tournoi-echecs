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

from controllers.factory import Factory
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
        new_player_dict = {}
        identifier = self.ask_player_identifier()
        new_player_dict['identifier'] = identifier
        last_name = self.ask_player_last_name()
        new_player_dict['last_name'] = last_name
        first_name = self.ask_player_first_name()
        new_player_dict['first_name'] = first_name
        birthdate = self.ask_player_birthdate()
        new_player_dict['birthdate'] = birthdate
        gender = self.ask_player_gender()
        new_player_dict['gender'] = gender
        ranking = self.ask_player_ranking()
        new_player_dict['ranking'] = ranking
        print(new_player_dict)
        print(f"\nNew Player Information\n"
              f"Identifier: {identifier}\n"
              f"Last Name: {last_name}\n"
              f"First Name: {first_name}\n"
              f"Birthdate: {birthdate}\n"
              f"Gender: {gender}\n"
              f"Ranking: {ranking}\n")
        player_factory = Factory(Player)
        new_player = player_factory.create(**new_player_dict)
        print(player_factory.registry)
        return new_player

        # Player: Pour la Player Database
        #  'identifier', 'last_name', 'first_name', 'birthdate', 'gender', 'ranking'

    def ask_player_identifier(self):
        """
        This method asks for the player's identifier
        """
        return input("Enter Player ID: ")

    def ask_player_last_name(self):
        """
        This method asks for the player's last name
        """
        return input("Enter Player Last Name: ")

    def ask_player_first_name(self):
        """
        This method asks for the player's first name
        """
        return input("Enter Player First Name: ")

    def ask_player_birthdate(self):
        """
        This method asks for the player's birthdate
        """
        return input("Enter Player Birthdate(YYYY-MM-DD): ")

    def ask_player_gender(self):
        """
        This method asks for the player's gender
        """
        return input("Enter Player Gender: ")

    def ask_player_ranking(self):
        """
        This method asks for the player's ranking
        """
        return int(input("Enter Player Ranking: "))

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
