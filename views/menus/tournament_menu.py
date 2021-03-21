# coding=utf-8

from controllers.factory import Factory
from models.tournament import Tournament
from views.menus.menu import Menu
from views.menus.list_tournaments_menu import ListTournamentsMenu

import views.menus.home_menu as home_menu

"""
View file for the Tournament Management Menu.
"""


class TournamentMenu(Menu):
    """
    This class manages a menu to navigate through the Tournament Management.
    """

    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='-Tournaments Menu-',
                         previous_page=home_menu.HomeMenu())
        specific_menu_choices = [self.list_all, self.add_new_tournament,
                                 self.save_tournament, self.load_tournament]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def list_all(self):  # redirige vers list_tournaments_menu, à mutualiser ? rendre générique, pareil que le list_all de player
        ListTournamentsMenu().run()

    # defs à ecrire !
    def add_new_tournament(self):
        pass


    def save_tournament(self):
        pass

    def load_tournament(self):
        pass



    # defs à reprendre et reutiliser autre part

    # Tournament : Pour la création des tournois
    # 'name', 'location', 'start_date', 'end_date', 'players_identifier',
    # 'time_control', 'description', 'rounds_list', 'rounds'


    def add_new_tournament(self):
        """
        This method asks all the required info about a specific tournament.
        It returns the info as a dict
        """
        name = self.ask_tournament_name()
        location = self.ask_tournament_location()
        players = self.ask_tournament_players()
        time_control = self.ask_tournament_time_control()
        description = self.ask_tournament_description()
        new_tournament_dict = {
            'name': name,
            'location': location,
            'players': players,
            'time_control': time_control,
            'description': description
        }
        print(f'\nTournament Information\n', new_tournament_dict)
        tournament_factory = Factory(Tournament)
        new_tournament = tournament_factory.create(**new_tournament_dict)
        print(tournament_factory.registry)
        print(new_tournament.__dict__)
        return new_tournament

    def ask_tournament_name(self):
        """
        This method asks for the tournament's name
        """
        return input("Enter Tournament name: ")

    def ask_tournament_location(self):
        """
        This method asks for the tournament's location
        """
        return input("Enter Tournament Location: ")

    def ask_tournament_players(self): # ce serait sympa de pouvoir faire une recherche !
        """
        This method asks for the list of 8 players for the tournament
        """
        tournament_players = []
        n = 1
        while n < 9:
            _input = input(f"Enter Player ID {n}/8:")
            tournament_players.append(_input)
            n += 1
        return tournament_players

    def ask_tournament_time_control(self):
        """
        This method asks for the time control format of the tournament
        """
        return input("Enter Time Control Format: ")

    def ask_tournament_description(self):
        """
        This method asks for a description of the tournament
        """
        return input("Enter Tournament Description: ")



if __name__ == '__main__':
    TournamentMenu().run()
