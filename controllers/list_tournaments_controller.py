# coding=utf-8
from models.models_utils.superfactory import super_factory as sf
from models.tournament import Tournament
from controllers.controller import Controller
from views.menus.list_tournaments_menu import ListTournamentsMenu


class ListTournamentsCtrl(Controller):
    def __init__(self):
        self.menu = ListTournamentsMenu()

    def list_all_tournaments(self):
        tournaments_list = []
        for identifier in sf.factories[Tournament].registry:
            tournament_obj = sf.factories[Tournament].registry[identifier]
            tournaments_list.append(tournament_obj)
        sorted_by_start_date = sorted(tournaments_list, key=lambda x: x.start_date)
        return sorted_by_start_date

    def sort_by_name(self):
        """
        This function lists the tournament instances alphabetically sorted by name
        """
        tournaments_list = []
        for identifier in sf.factories[Tournament].registry:
            tournament_obj = sf.factories[Tournament].registry[identifier]
            tournaments_list.append(tournament_obj)
        sorted_by_name = sorted(tournaments_list, key=lambda x: x.name)
        return sorted_by_name

    def sort_by_location(self):
        """
        This function lists the tournament instances alphabetically sorted by location
        """
        tournaments_list = []
        for identifier in sf.factories[Tournament].registry:
            tournament_obj = sf.factories[Tournament].registry[identifier]
            tournaments_list.append(tournament_obj)
        sorted_by_location = sorted(tournaments_list, key=lambda x: x.location)
        return sorted_by_location

    def sort_by_start_date(self): # doublon avec list_all_tournaments (seul l'ordre change, voir lequel je prends)
        """
        This function lists the tournament instances sorted by reverse chronological start date
        """
        tournaments_list = []
        for identifier in sf.factories[Tournament].registry:
            tournament_obj = sf.factories[Tournament].registry[identifier]
            tournaments_list.append(tournament_obj)
        sorted_by_start_date = sorted(tournaments_list, key=lambda x: x.start_date, reverse=True)
        return sorted_by_start_date

    def search_by_id(self, search):
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

    def select_one(self): # returns selected tournament
        pass