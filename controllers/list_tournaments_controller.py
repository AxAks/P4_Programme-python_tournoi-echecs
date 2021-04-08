# coding=utf-8

from models.models_utils.superfactory import super_factory as sf
from models.models_utils.tournament_manager import list_registered_tournaments
from models.tournament import Tournament
from controllers.controller import Controller
from views.menus.list_tournaments_menu import ListTournamentsMenu


class ListTournamentsCtrl(Controller):
    """
    Controller class for the menu that lists Tournaments
    """
    def __init__(self):
        self.menu = ListTournamentsMenu()

    def sort_by_start_date(self):
        """
        This function lists the tournament instances sorted by start date
        """
        tournaments_list = list_registered_tournaments()
        sorted_by_start_date = sorted(tournaments_list, key=lambda x: x.start_date)
        return sorted_by_start_date

    def sort_by_name(self):
        """
        This function lists the tournament instances alphabetically sorted by name
        """
        tournaments_list = list_registered_tournaments()
        sorted_by_name = sorted(tournaments_list, key=lambda x: x.name)
        return sorted_by_name

    def sort_by_location(self):
        """
        This function lists the tournament instances alphabetically sorted by location
        """
        tournaments_list = list_registered_tournaments()
        sorted_by_location = sorted(tournaments_list, key=lambda x: x.location)
        return sorted_by_location

    def search_by_id(self, search):  # voir tournament manager : search_one_tournament
        """
        This function lists the tournament instances matching the given input
        (identifier: Name, Location, Start date, End date)
        """
        results = sf.factories[Tournament].search(search)
        found_tournaments_list = []
        for identifier in results:
            tournament_obj = sf.factories[Tournament].registry[identifier]
            found_tournaments_list.append(tournament_obj)
        return found_tournaments_list

    def select_one(self):  # returns selected tournament, à faire
        """
        This function enables to select a specific tournament in the registered tournaments list
        """
        pass