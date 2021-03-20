# coding=utf-8

from controllers.factory import Factory
from models.player import Player
from views.menus.list_players_menu import ListPlayerMenu
from views.menus.menu import Menu
import views.menus.home_menu as home_menu  # import du module plutot que la classe pour eviter le pb d'import circulaire


"""
View file for the Player Database Management Menu.
"""


class PlayerMenu(Menu):
    """
    This class manages a menu to navigate through the Player Database Management.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='-Players Menu-')
        specific_menu_choices = [self.list_all, self.add_new_player, self.edit_player]
        [self.choices.append(choice) for choice in specific_menu_choices]


    #  on recupère def run() et def back() (avec un if) via l'héritage de Menu car il sont toujours identiques


    #defs à ecrire !
    def list_all(self): # directs to another menu Class ListPlayers , mutualiser avec list_all de tournaments dans menu
        ListPlayerMenu().run()

    def edit_player(self):
        pass

#defs à revoir
    def add_new_player(self):  # utiliser pour formulaire ?
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


if __name__ == '__main__':
    PlayerMenu().run()
