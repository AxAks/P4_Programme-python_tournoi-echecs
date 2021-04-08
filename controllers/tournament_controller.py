# coding=utf-8

"""
Controller file for Tournament
"""
from controllers.controller import Controller
from models.tournament import Tournament
from models.models_utils.superfactory import super_factory as sf
from views.forms.add_tournament_form import NewTournamentForm
from views.menus.tournaments_menu import TournamentsMenu


class TournamentCtrl(Controller):
    def __init__(self):
        self.menu = TournamentsMenu()

    def run(self):
        """
        This method displays the menu and responds to choices made.
        """
        valid_choices = range(len(TournamentsMenu().choices))
        choice = -1
        while choice not in valid_choices:
            TournamentsMenu().show()
            _input = input('Enter an option: ')
            try:
                choice = int(_input)
                if choice not in valid_choices:
                    print(f'-> "{choice}" is not a valid choice <-')
            except ValueError:
                print(f'-> "{_input}" is not a valid choice <-')

        action = TournamentsMenu().choices[choice]
        action()

    def add_tournament(self) -> Tournament:
        """
        this method creates a new player entry in the registry.
        """
        new_tournament_dict = NewTournamentForm().add_new_tournament()
        new_tournament = sf.factories[Tournament].create(**new_tournament_dict)
        return new_tournament
