# coding=utf-8

import sys

from controllers.factory import Factory
from models.player import Player
from views.menus.menu import Menu

"""
View file for the Player Database Management Menu.
"""


class PlayerMenu(Menu):
    """
    This class manages a menu to navigate through the Player Database Management.
    """
    def __init__(self):
        super().__init__()  # initialise les choix généraux depuis Menu
        specific_menu_choices = [self.list_all_players, self.add_new_player, self.edit_player]  # liste des choix spécifiques de PlayerMenu
        [self.choices.append(choice) for choice in specific_menu_choices]  # ajoute les spécificités de PlayerMenu à la liste de choix


    #  on recupère run() via l'héritage de Menu


    def player_menu(self):  # à réécrire de facon specifique
        """
        This method displays the different options of the menu: Player Database.
        """
        pass


    #defs à ecrire !

    def add_new_player(self):
        pass

    def list_all_players(self):
        pass

    def edit_player(self):
        pass

    def save_tournament(self):
        pass

    def load_torunament(self):
        pass




#defs à revoir
    def display_all_player(self):
        pass

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


if __name__ == '__main__':
    PlayerMenu().run()
