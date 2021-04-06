# coding=utf-8
from models.models_utils.superfactory import super_factory as sf
from models.tournament import Tournament
from controllers.controller import Controller
from views.menus.list_tournaments_menu import ListTournamentMenu


class ListTournamentsCtrl(Controller):
    def __init__(self):
        self.menu = ListTournamentMenu()

    def list_all_tournaments(self):
        tournaments_list = []
        for identifier in sf.factories[Tournament].registry:
            tournament_obj = sf.factories[Tournament].registry[identifier]
            tournaments_list.append(tournament_obj)
        sorted_by_start_date = sorted(tournaments_list, key=lambda x: x.start_date)
        return sorted_by_start_date