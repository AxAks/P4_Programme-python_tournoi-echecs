# coding=utf-8
from models.models_utils.supermanager import super_manager as sm
from models.models_utils.tournament_manager import TournamentManager
from models.tournament import Tournament
from controllers.controller import Controller
from views.forms.new_tournament_form import NewTournamentForm
from views.menus.list_tournaments_menu import ListTournamentsMenu


class ListTournamentsCtrl(Controller):
    """
    Controller class for the menu that lists Tournaments
    """

    def __init__(self):
        self.menu = ListTournamentsMenu()

    def add_tournament(self) -> Tournament:
        """
        this method creates a new tournament entry in the registry.
        """
        new_tournament_dict = NewTournamentForm().add_new()
        new_tournament = sm.managers[Tournament].create(**new_tournament_dict)  # gérer l'erreur de dates etc ici !
        return new_tournament

    def sort_by_start_date(self) -> list:
        """
        This function lists the tournament instances sorted by start date
        """
        tournaments_list = TournamentManager().list_registered_tournaments()
        sorted_by_start_date = sorted(tournaments_list, key=lambda x: x.start_date)
        return sorted_by_start_date

    def sort_by_name(self) -> list:
        """
        This function lists the tournament instances alphabetically sorted by name
        """
        tournaments_list = TournamentManager().list_registered_tournaments()
        sorted_by_name = sorted(tournaments_list, key=lambda x: x.name)
        return sorted_by_name

    def sort_by_location(self) -> list:
        """
        This function lists the tournament instances alphabetically sorted by location
        """
        tournaments_list = TournamentManager().list_registered_tournaments()
        sorted_by_location = sorted(tournaments_list, key=lambda x: x.location)
        return sorted_by_location

    def search_by_id(self, search) -> list:
        """
        This function lists the tournament instances matching the given input
        (identifier: Name, Location, Start date, End date)
        """
        results = sm.managers[Tournament].search(search)
        found_tournaments_list = []
        for identifier in results:
            tournament_obj = sm.managers[Tournament].registry[identifier]
            found_tournaments_list.append(tournament_obj)
        return found_tournaments_list

    def select_one(self):
        """
        This function enables to select a specific tournament in the registered tournaments list
        """
        _input = input('Search a tournament by name, location or dates: ')
        selected_tournament = TournamentManager().search_one(_input)
        return selected_tournament
