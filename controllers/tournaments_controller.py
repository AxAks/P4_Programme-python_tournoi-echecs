# coding=utf-8

from utils import clear_terminal
from models.tournament import Tournament
from models.models_utils.supermanager import super_manager as sm
from controllers import list_tournaments_controller
from controllers.controller import Controller
from views.forms.new_tournament_form import NewTournamentForm
from views.menus.tournaments_menu import TournamentsMenu


class TournamentCtrl(Controller):
    """
    Controller class for the Tournament Menu
    """

    def __init__(self):
        self.menu = TournamentsMenu()

    def add_tournament(self) -> Tournament:
        """
        this method creates a new tournament entry in the registry.
        """
        new_tournament_dict = NewTournamentForm().add_new()
        new_tournament = sm.managers[Tournament].create(**new_tournament_dict)  # gérer l'erreur de dates etc ici !
        return new_tournament

    def to_tournaments_list(self) -> None:
        """
        This method redirects to the Tournaments Lists Menu
        """
        clear_terminal()
        list_tournaments_controller.ListTournamentsCtrl().run()
