# coding=utf-8

from utils import clear_terminal
from models.tournament import Tournament
from models.models_utils.superfactory import super_factory as sf
from controllers import list_tournaments_controller
from controllers.controller import Controller
from views.forms.add_tournament_form import NewTournamentForm
from views.menus.tournaments_menu import TournamentsMenu


class TournamentCtrl(Controller):
    """
    Controller class for the Tournament Menu
    """

    def __init__(self):
        self.menu = TournamentsMenu()

    def add_tournament(self) -> Tournament:
        """
        this method creates a new player entry in the registry.
        """
        new_tournament_dict = NewTournamentForm().add_new_tournament()
        new_tournament = sf.factories[Tournament].create(**new_tournament_dict)
        return new_tournament

    def to_tournaments_list(self) -> None:
        clear_terminal()
        list_tournaments_controller.ListTournamentsCtrl().run()